from __future__ import annotations

import argparse
import json
import sqlite3
import time
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT_TAX_ID = 33208
BATCH_SIZE = 200
API_BASE = "https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/"

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "ncbi-animalia-full-tree.sqlite"
OUT_PATH = BASE_DIR / "ncbi-animalia-full-tree.jsonl"
META_PATH = BASE_DIR / "ncbi-animalia-full-tree-meta.json"


def rank_label(rank: str | None) -> str:
    if not rank:
        return ""
    return rank.replace("_", " ").title().replace(" ", "")


def fetch_records(ids: list[int]) -> list[dict[str, Any]]:
    url = API_BASE + ",".join(str(tax_id) for tax_id in ids)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "taxonomic-ranker-animalia-full-tree/0.1"},
    )

    last_error: Exception | None = None
    for attempt in range(1, 5):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                payload = json.loads(response.read().decode("utf-8"))
            return [
                node["taxonomy"]
                for node in payload.get("taxonomy_nodes", [])
                if "taxonomy" in node
            ]
        except Exception as error:
            last_error = error
            if attempt < 4:
                time.sleep(2 * attempt)

    raise RuntimeError(f"Failed to fetch {len(ids)} NCBI taxonomy records: {last_error}") from last_error


def connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.execute("pragma journal_mode = wal")
    connection.execute("pragma synchronous = normal")
    connection.execute("""
        create table if not exists records (
            id integer primary key,
            parent_id integer,
            depth integer not null,
            rank text not null,
            official_name text not null,
            common_name text not null,
            genbank_common_name text not null,
            blast_name text not null,
            children_json text not null,
            fetched_at text not null
        )
    """)
    connection.execute("""
        create table if not exists frontier (
            id integer primary key,
            parent_id integer,
            depth integer not null
        )
    """)
    connection.execute("create index if not exists idx_records_parent on records(parent_id)")
    connection.execute("create index if not exists idx_records_depth on records(depth)")
    return connection


def initialize_frontier(connection: sqlite3.Connection) -> None:
    existing = connection.execute("select count(*) from records").fetchone()[0]
    queued = connection.execute("select count(*) from frontier").fetchone()[0]
    if existing == 0 and queued == 0:
        connection.execute(
            "insert or ignore into frontier (id, parent_id, depth) values (?, ?, ?)",
            (ROOT_TAX_ID, None, 0),
        )
        connection.commit()


def next_frontier_batch(connection: sqlite3.Connection, batch_size: int) -> list[tuple[int, int | None, int]]:
    return [
        (int(row[0]), None if row[1] is None else int(row[1]), int(row[2]))
        for row in connection.execute(
            "select id, parent_id, depth from frontier order by depth, id limit ?",
            (batch_size,),
        ).fetchall()
    ]


def store_records(
    connection: sqlite3.Connection,
    requested: list[tuple[int, int | None, int]],
    records: list[dict[str, Any]],
) -> int:
    requested_by_id = {tax_id: (parent_id, depth) for tax_id, parent_id, depth in requested}
    fetched_at = datetime.now(timezone.utc).isoformat()
    inserted = 0

    with connection:
        for taxonomy in records:
            tax_id = int(taxonomy["tax_id"])
            parent_id, depth = requested_by_id[tax_id]
            children = [int(child_id) for child_id in taxonomy.get("children", []) or []]
            connection.execute(
                """
                insert or ignore into records (
                    id, parent_id, depth, rank, official_name, common_name,
                    genbank_common_name, blast_name, children_json, fetched_at
                )
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    tax_id,
                    parent_id,
                    depth,
                    rank_label(taxonomy.get("rank")),
                    taxonomy.get("organism_name", "") or "",
                    taxonomy.get("common_name", "") or "",
                    taxonomy.get("genbank_common_name", "") or "",
                    taxonomy.get("blast_name", "") or "",
                    json.dumps(children, separators=(",", ":")),
                    fetched_at,
                ),
            )
            if connection.total_changes:
                inserted += 1

            for child_id in children:
                child_known = connection.execute(
                    "select 1 from records where id = ?",
                    (child_id,),
                ).fetchone()
                if child_known is None:
                    connection.execute(
                        "insert or ignore into frontier (id, parent_id, depth) values (?, ?, ?)",
                        (child_id, tax_id, depth + 1),
                    )

            connection.execute("delete from frontier where id = ?", (tax_id,))

        fetched_ids = {int(taxonomy["tax_id"]) for taxonomy in records}
        for tax_id, _, _ in requested:
            if tax_id not in fetched_ids:
                connection.execute("delete from frontier where id = ?", (tax_id,))

    return inserted


def crawl(connection: sqlite3.Connection, *, max_batches: int | None = None) -> None:
    initialize_frontier(connection)
    batch_number = 0
    started = time.time()

    while True:
        requested = next_frontier_batch(connection, BATCH_SIZE)
        if not requested:
            break
        if max_batches is not None and batch_number >= max_batches:
            break

        records = fetch_records([tax_id for tax_id, _, _ in requested])
        store_records(connection, requested, records)
        batch_number += 1

        if batch_number == 1 or batch_number % 25 == 0:
            record_count = connection.execute("select count(*) from records").fetchone()[0]
            frontier_count = connection.execute("select count(*) from frontier").fetchone()[0]
            common_count = connection.execute(
                "select count(*) from records where genbank_common_name != ''"
            ).fetchone()[0]
            elapsed = time.time() - started
            print(
                f"batches={batch_number} records={record_count} "
                f"frontier={frontier_count} common={common_count} "
                f"elapsed={elapsed:.1f}s",
                flush=True,
            )


def dump_jsonl(connection: sqlite3.Connection) -> None:
    frontier_count = connection.execute("select count(*) from frontier").fetchone()[0]
    if frontier_count:
        print(f"Frontier still has {frontier_count} nodes; not writing final JSONL yet.")
        return

    rows = connection.execute(
        """
        select id, parent_id, depth, rank, official_name, common_name,
               genbank_common_name, blast_name, children_json
        from records
        order by depth, id
        """
    )

    rank_counts: Counter[str] = Counter()
    common_count = 0
    total = 0
    max_depth = 0
    with OUT_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            children = json.loads(row[8])
            node = {
                "id": int(row[0]),
                "parentId": None if row[1] is None else int(row[1]),
                "depth": int(row[2]),
                "rank": row[3],
                "officialName": row[4],
                "commonName": row[5],
                "genbankCommonName": row[6],
                "blastName": row[7],
                "children": children,
            }
            handle.write(json.dumps(node, ensure_ascii=True, separators=(",", ":")) + "\n")
            rank_counts[node["rank"] or "(blank)"] += 1
            if node["genbankCommonName"]:
                common_count += 1
            total += 1
            max_depth = max(max_depth, node["depth"])

    meta = {
        "source": "NCBI Datasets taxonomy JSON",
        "sourceUrl": API_BASE + str(ROOT_TAX_ID),
        "rootTaxId": ROOT_TAX_ID,
        "rootName": "Metazoa / Animalia",
        "nodeCount": total,
        "genbankCommonNameCount": common_count,
        "maxDepth": max_depth,
        "rankCounts": dict(rank_counts.most_common()),
        "jsonlFile": OUT_PATH.name,
        "sqliteCache": DB_PATH.name,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "fields": [
            "id",
            "parentId",
            "depth",
            "rank",
            "officialName",
            "commonName",
            "genbankCommonName",
            "blastName",
            "children",
        ],
    }
    META_PATH.write_text(json.dumps(meta, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Wrote {total} JSONL nodes to {OUT_PATH}")
    print(f"Wrote metadata to {META_PATH}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-batches", type=int, default=None)
    parser.add_argument("--dump-only", action="store_true")
    args = parser.parse_args()

    connection = connect()
    if not args.dump_only:
        crawl(connection, max_batches=args.max_batches)
    dump_jsonl(connection)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
