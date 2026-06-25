from __future__ import annotations

import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


ROOT_TAX_ID = 7711
MAX_DEPTH = 4
MAX_ENTRIES = 20_000

OUT_PATH = Path(__file__).with_name("ncbi-chordata-standard-ranks.json")
BASE_URL = "https://www.ncbi.nlm.nih.gov/datasets/taxonomy/browser/fragment/"


class TaxonomyTreeParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: list[dict[str, object]] = []
        self._row: dict[str, object] | None = None
        self._capture: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name: value or "" for name, value in attrs}
        classes = attr.get("class", "").split()

        if tag == "tr" and "taxonomy-tree2-node" in classes:
            parent_id = attr.get("data-parent-id", "")
            self._row = {
                "id": int(attr["data-tax-id"]),
                "parentId": None if parent_id == "null" else int(parent_id),
                "depth": int(attr["data-depth"]),
                "_rankText": [],
                "_nameText": [],
                "_commonText": [],
            }
            return

        if self._row is None or tag != "span":
            return

        if "taxonomy-tree2-rank-prefix" in classes:
            self._capture = "_rankText"
        elif "taxonomy-tree2-scientific-name" in classes:
            self._capture = "_nameText"
        elif "taxonomy-tree2-common-name" in classes:
            self._capture = "_commonText"

    def handle_data(self, data: str) -> None:
        if self._row is not None and self._capture:
            self._row[self._capture].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "span":
            self._capture = None
            return

        if tag == "tr" and self._row is not None:
            rank = "".join(self._row.pop("_rankText")).strip().rstrip(":")
            name = " ".join("".join(self._row.pop("_nameText")).split())
            common = " ".join("".join(self._row.pop("_commonText")).split())
            if common.startswith("(") and common.endswith(")"):
                common = common[1:-1].strip()

            self._row["rank"] = rank
            self._row["officialName"] = name
            self._row["genbankCommonName"] = common
            self.rows.append(self._row)
            self._row = None
            self._capture = None


def fetch_tree_html() -> tuple[str, str]:
    params = {
        "taxon": ROOT_TAX_ID,
        "rank_limit": "standard",
        "exclude_extinct": "true",
        "levels": MAX_DEPTH,
    }
    source_url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        source_url,
        headers={"User-Agent": "taxonomic-ranker-data-builder/0.1"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return source_url, payload["tree_html"]


def parse_rows(tree_html: str) -> list[dict[str, object]]:
    parser = TaxonomyTreeParser()
    parser.feed(tree_html)

    seen: set[int] = set()
    unique_rows: list[dict[str, object]] = []
    for order, row in enumerate(parser.rows):
        tax_id = int(row["id"])
        if tax_id in seen:
            continue
        seen.add(tax_id)
        row["sourceOrder"] = order
        unique_rows.append(row)

    return sorted(unique_rows, key=lambda row: (int(row["depth"]), int(row["sourceOrder"])))


def main() -> int:
    source_url, tree_html = fetch_tree_html()
    rows = parse_rows(tree_html)

    truncated = len(rows) > MAX_ENTRIES
    nodes = rows[:MAX_ENTRIES]
    for node in nodes:
        node.pop("sourceOrder", None)

    layers = Counter(int(node["depth"]) for node in nodes)
    data = {
        "meta": {
            "source": "NCBI Taxonomy Browser fragment",
            "sourceUrl": source_url,
            "rootTaxId": ROOT_TAX_ID,
            "rankLimit": "standard",
            "excludeExtinct": True,
            "maxDepth": MAX_DEPTH,
            "maxEntries": MAX_ENTRIES,
            "entryCount": len(nodes),
            "truncated": truncated,
            "layers": {str(depth): layers[depth] for depth in sorted(layers)},
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "fields": ["id", "parentId", "depth", "rank", "officialName", "genbankCommonName"],
        },
        "nodes": nodes,
    }

    OUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(nodes)} nodes to {OUT_PATH}")
    print(f"Layer counts: {data['meta']['layers']}")
    if truncated:
        print(f"Truncated at {MAX_ENTRIES} entries", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
