from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


THRESHOLD = 100
ROOT_TAX_ID = 33208

BASE_DIR = Path(__file__).resolve().parent
FULL_TREE_PATH = BASE_DIR / "ncbi-animalia-full-tree.jsonl"
OUT_PATH = BASE_DIR / "ncbi-animalia-svelte-tree.json"
COUNTS_PATH = BASE_DIR / "ncbi-animalia-svelte-tree-counts.json"

NAME_SOURCES = {
    "genbank": {
        "jsonField": "genbankCommonName",
        "includedBy": "genbankCommonName",
        "outPath": OUT_PATH,
        "countsPath": COUNTS_PATH,
    },
    "common": {
        "jsonField": "commonName",
        "includedBy": "commonName",
        "outPath": BASE_DIR / "ncbi-animalia-svelte-tree-common-name.json",
        "countsPath": BASE_DIR / "ncbi-animalia-svelte-tree-common-name-counts.json",
    },
    "genbank-common": {
        "jsonField": "genbankCommonNameOrCommonName",
        "includedBy": "genbankCommonNameOrCommonName",
        "outPath": BASE_DIR / "ncbi-animalia-svelte-tree-genbank-common.json",
        "countsPath": BASE_DIR / "ncbi-animalia-svelte-tree-genbank-common-counts.json",
    },
    "genbank-common-nonleaf": {
        "jsonField": "genbankCommonNameOrCommonName",
        "includedBy": "genbankCommonNameOrCommonName",
        "outPath": BASE_DIR / "ncbi-animalia-svelte-tree-genbank-common-nonleaf.json",
        "countsPath": BASE_DIR / "ncbi-animalia-svelte-tree-genbank-common-nonleaf-counts.json",
        "pruneCommonNameFallbackLeavesBeforeCondense": True,
    },
}


def load_full_tree() -> tuple[
    dict[int, int | None],
    dict[int, int],
    dict[int, tuple[str, str, str, str]],
]:
    parent_by_id: dict[int, int | None] = {}
    depth_by_id: dict[int, int] = {}
    info_by_id: dict[int, tuple[str, str, str, str]] = {}

    with FULL_TREE_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            node = json.loads(line)
            tax_id = int(node["id"])
            parent_by_id[tax_id] = node["parentId"]
            depth_by_id[tax_id] = int(node["depth"])
            info_by_id[tax_id] = (
                node.get("rank", "") or "",
                node.get("officialName", "") or "",
                node.get("commonName", "") or "",
                node.get("genbankCommonName", "") or "",
            )

    return parent_by_id, depth_by_id, info_by_id


def nearest_retained_ancestor(
    tax_id: int,
    parent_by_id: dict[int, int | None],
    retained_ids: set[int],
    memo: dict[int, int | None],
) -> int | None:
    if tax_id in memo:
        return memo[tax_id]

    parent_id = parent_by_id.get(tax_id)
    while parent_id is not None:
        if parent_id in retained_ids:
            memo[tax_id] = parent_id
            return parent_id
        parent_id = parent_by_id.get(parent_id)

    memo[tax_id] = None
    return None


def make_node(
    tax_id: int,
    *,
    parent_id: int | None,
    parent_by_id: dict[int, int | None],
    depth_by_id: dict[int, int],
    info_by_id: dict[int, tuple[str, str, str, str]],
    included_by: list[str],
    name_field: str,
) -> dict[str, Any]:
    rank, official_name, common_name, genbank_common_name = info_by_id[tax_id]
    if name_field == "commonName":
        display_name = common_name
    elif name_field == "genbankCommonNameOrCommonName":
        display_name = genbank_common_name or common_name
    else:
        display_name = genbank_common_name

    return {
        "id": tax_id,
        "parentId": parent_id,
        "ncbiParentId": parent_by_id.get(tax_id),
        "depth": depth_by_id[tax_id],
        "rank": rank,
        "officialName": official_name,
        "commonName": common_name,
        "genbankCommonName": genbank_common_name,
        "displayName": display_name,
        "includedBy": included_by,
    }


def build_common_name_tree(
    parent_by_id: dict[int, int | None],
    depth_by_id: dict[int, int],
    info_by_id: dict[int, tuple[str, str, str, str]],
    named_ids: set[int],
    name_field: str,
    included_by_name: str,
) -> tuple[dict[int, dict[str, Any]], dict[int, set[int]]]:
    nodes: dict[int, dict[str, Any]] = {}
    children_by_parent: dict[int, set[int]] = defaultdict(set)
    memo: dict[int, int | None] = {}

    for tax_id in sorted(named_ids, key=lambda item: (depth_by_id[item], item)):
        parent_id = nearest_retained_ancestor(tax_id, parent_by_id, named_ids, memo)
        included_by = [included_by_name]
        if name_field == "genbankCommonNameOrCommonName":
            included_by = ["genbankCommonName"] if info_by_id[tax_id][3] else ["commonNameFallback"]
        nodes[tax_id] = make_node(
            tax_id,
            parent_id=parent_id,
            parent_by_id=parent_by_id,
            depth_by_id=depth_by_id,
            info_by_id=info_by_id,
            included_by=included_by,
            name_field=name_field,
        )
        if parent_id is not None:
            children_by_parent[parent_id].add(tax_id)

    return nodes, children_by_parent


def path_candidate_sets(
    *,
    parent_id: int,
    child_ids: set[int],
    parent_by_id: dict[int, int | None],
) -> dict[int, set[int]]:
    candidates: dict[int, set[int]] = defaultdict(set)

    for child_id in child_ids:
        current_id = parent_by_id.get(child_id)
        seen: set[int] = set()
        while current_id is not None and current_id not in seen:
            if current_id == parent_id:
                break
            seen.add(current_id)
            candidates[current_id].add(child_id)
            current_id = parent_by_id.get(current_id)

    return candidates


def best_group_candidate(
    *,
    parent_id: int,
    child_ids: set[int],
    parent_by_id: dict[int, int | None],
    depth_by_id: dict[int, int],
) -> tuple[int, set[int]] | None:
    candidates = path_candidate_sets(
        parent_id=parent_id,
        child_ids=child_ids,
        parent_by_id=parent_by_id,
    )
    useful = [
        (candidate_id, grouped_children)
        for candidate_id, grouped_children in candidates.items()
        if len(grouped_children) > 1
    ]
    if not useful:
        return None

    return min(
        useful,
        key=lambda item: (
            len(item[1]),
            -depth_by_id[item[0]],
            item[0],
        ),
    )


def insert_group(
    *,
    group_id: int,
    parent_id: int,
    grouped_children: set[int],
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
    parent_by_id: dict[int, int | None],
    depth_by_id: dict[int, int],
    info_by_id: dict[int, tuple[str, str, str, str]],
    name_field: str,
) -> bool:
    inserted = False
    if group_id not in nodes:
        nodes[group_id] = make_node(
            group_id,
            parent_id=parent_id,
            parent_by_id=parent_by_id,
            depth_by_id=depth_by_id,
            info_by_id=info_by_id,
            included_by=["intermediaryMerge"],
            name_field=name_field,
        )
        children_by_parent[parent_id].add(group_id)
        inserted = True

    for child_id in grouped_children:
        if child_id == group_id:
            continue
        old_parent_id = nodes[child_id]["parentId"]
        if old_parent_id is not None:
            children_by_parent[old_parent_id].discard(child_id)
        nodes[child_id]["parentId"] = group_id
        children_by_parent[group_id].add(child_id)

    return inserted


def condense_tree(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
    parent_by_id: dict[int, int | None],
    depth_by_id: dict[int, int],
    info_by_id: dict[int, tuple[str, str, str, str]],
    name_field: str,
) -> dict[int, int]:
    queue = deque(
        sorted(
            (tax_id for tax_id in nodes if len(children_by_parent[tax_id]) > THRESHOLD),
            key=lambda item: len(children_by_parent[item]),
            reverse=True,
        )
    )
    exhausted: set[int] = set()

    while queue:
        parent_id = queue.popleft()
        if parent_id in exhausted or parent_id not in nodes:
            continue

        while len(children_by_parent[parent_id]) > THRESHOLD:
            candidate = best_group_candidate(
                parent_id=parent_id,
                child_ids=children_by_parent[parent_id],
                parent_by_id=parent_by_id,
                depth_by_id=depth_by_id,
            )
            if candidate is None:
                exhausted.add(parent_id)
                break

            group_id, grouped_children = candidate
            insert_group(
                group_id=group_id,
                parent_id=parent_id,
                grouped_children=grouped_children,
                nodes=nodes,
                children_by_parent=children_by_parent,
                parent_by_id=parent_by_id,
                depth_by_id=depth_by_id,
                info_by_id=info_by_id,
                name_field=name_field,
            )

            if len(children_by_parent[group_id]) > THRESHOLD:
                queue.append(group_id)

        if len(children_by_parent[parent_id]) > THRESHOLD and parent_id not in exhausted:
            queue.append(parent_id)

    return {tax_id: len(children_by_parent[tax_id]) for tax_id in exhausted}


def prune_common_name_fallback_leaves(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
) -> list[dict[str, Any]]:
    pruned: list[dict[str, Any]] = []

    while True:
        leaf_ids = [
            tax_id
            for tax_id, node in nodes.items()
            if node["includedBy"] == ["commonNameFallback"]
            and not any(child_id in nodes for child_id in children_by_parent[tax_id])
        ]
        if not leaf_ids:
            break

        for tax_id in sorted(leaf_ids, key=lambda item: (nodes[item]["depth"], item), reverse=True):
            if tax_id not in nodes:
                continue
            node = nodes[tax_id]
            parent_id = node["parentId"]
            pruned.append({
                "id": tax_id,
                "parentId": parent_id,
                "rank": node["rank"],
                "officialName": node["officialName"],
                "displayName": node["displayName"],
            })
            if parent_id is not None:
                children_by_parent[parent_id].discard(tax_id)
            nodes.pop(tax_id, None)
            children_by_parent.pop(tax_id, None)

    return pruned


def count_leaf_descendants(
    tax_id: int,
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
    memo: dict[int, int],
) -> int:
    if tax_id in memo:
        return memo[tax_id]

    children = [child_id for child_id in children_by_parent[tax_id] if child_id in nodes]
    if not children:
        memo[tax_id] = 1
        return 1

    memo[tax_id] = sum(
        count_leaf_descendants(child_id, nodes, children_by_parent, memo)
        for child_id in children
    )
    return memo[tax_id]


def subtree_ids(
    tax_id: int,
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
) -> list[int]:
    found: list[int] = []
    stack = [tax_id]
    while stack:
        current_id = stack.pop()
        if current_id not in nodes:
            continue
        found.append(current_id)
        stack.extend(children_by_parent[current_id])
    return found


def collapse_single_leaf_descendants(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
) -> list[dict[str, Any]]:
    leaf_counts: dict[int, int] = {}
    for tax_id in list(nodes):
        count_leaf_descendants(tax_id, nodes, children_by_parent, leaf_counts)

    collapses: list[dict[str, Any]] = []
    for tax_id in sorted(list(nodes), key=lambda item: (nodes[item]["depth"], item)):
        if tax_id not in nodes:
            continue
        if not nodes[tax_id]["displayName"]:
            continue

        child_ids = [child_id for child_id in children_by_parent[tax_id] if child_id in nodes]
        if len(child_ids) != 1 or leaf_counts[tax_id] != 1:
            continue

        child_id = child_ids[0]
        removed_ids = subtree_ids(child_id, nodes, children_by_parent)
        removed_root = nodes[child_id]
        collapses.append({
            "id": tax_id,
            "rank": nodes[tax_id]["rank"],
            "officialName": nodes[tax_id]["officialName"],
            "displayName": nodes[tax_id]["displayName"],
            "removedRootId": child_id,
            "removedRootRank": removed_root["rank"],
            "removedRootOfficialName": removed_root["officialName"],
            "removedRootDisplayName": removed_root["displayName"],
            "removedNodeCount": len(removed_ids),
        })

        children_by_parent[tax_id].discard(child_id)
        for removed_id in removed_ids:
            nodes.pop(removed_id, None)
            children_by_parent.pop(removed_id, None)

    return collapses


def collapse_single_child_chains(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
) -> list[dict[str, Any]]:
    collapses: list[dict[str, Any]] = []

    while True:
        collapsed_this_pass = False
        for tax_id in sorted(list(nodes), key=lambda item: (nodes[item]["depth"], item)):
            if tax_id not in nodes:
                continue
            child_ids = [child_id for child_id in children_by_parent[tax_id] if child_id in nodes]
            if len(child_ids) != 1:
                continue

            child_id = child_ids[0]
            grandchild_ids = [
                grandchild_id
                for grandchild_id in children_by_parent[child_id]
                if grandchild_id in nodes
            ]
            if not grandchild_ids:
                continue

            parent_id = nodes[tax_id]["parentId"]
            if parent_id is not None:
                children_by_parent[parent_id].discard(tax_id)
                children_by_parent[parent_id].add(child_id)
            nodes[child_id]["parentId"] = parent_id

            collapses.append({
                "removedId": tax_id,
                "removedRank": nodes[tax_id]["rank"],
                "removedOfficialName": nodes[tax_id]["officialName"],
                "removedDisplayName": nodes[tax_id]["displayName"],
                "keptId": child_id,
                "keptRank": nodes[child_id]["rank"],
                "keptOfficialName": nodes[child_id]["officialName"],
                "keptDisplayName": nodes[child_id]["displayName"],
                "keptChildCount": len(grandchild_ids),
            })

            nodes.pop(tax_id, None)
            children_by_parent.pop(tax_id, None)
            collapsed_this_pass = True
            break

        if not collapsed_this_pass:
            break

    return collapses


def promote_grandchildren_of_sparse_nodes(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
) -> list[dict[str, Any]]:
    promotions: list[dict[str, Any]] = []

    while True:
        promoted_this_pass = False
        for tax_id in sorted(list(nodes), key=lambda item: (nodes[item]["depth"], item)):
            if tax_id not in nodes:
                continue

            child_ids = [child_id for child_id in children_by_parent[tax_id] if child_id in nodes]
            if len(child_ids) not in {2, 3}:
                continue

            promotable_child_ids = [
                child_id
                for child_id in child_ids
                if any(grandchild_id in nodes for grandchild_id in children_by_parent[child_id])
            ]
            if not promotable_child_ids:
                continue

            promoted_children: list[dict[str, Any]] = []
            for child_id in sorted(
                promotable_child_ids,
                key=lambda item: (nodes[item]["depth"], nodes[item]["id"]),
            ):
                if child_id not in nodes:
                    continue
                grandchild_ids = [
                    grandchild_id
                    for grandchild_id in children_by_parent[child_id]
                    if grandchild_id in nodes
                ]
                if not grandchild_ids:
                    continue

                children_by_parent[tax_id].discard(child_id)
                for grandchild_id in grandchild_ids:
                    nodes[grandchild_id]["parentId"] = tax_id
                    children_by_parent[tax_id].add(grandchild_id)

                promoted_children.append({
                    "removedId": child_id,
                    "removedRank": nodes[child_id]["rank"],
                    "removedOfficialName": nodes[child_id]["officialName"],
                    "removedDisplayName": nodes[child_id]["displayName"],
                    "promotedGrandchildCount": len(grandchild_ids),
                })
                nodes.pop(child_id, None)
                children_by_parent.pop(child_id, None)

            if promoted_children:
                promotions.append({
                    "id": tax_id,
                    "rank": nodes[tax_id]["rank"],
                    "officialName": nodes[tax_id]["officialName"],
                    "displayName": nodes[tax_id]["displayName"],
                    "beforeChildCount": len(child_ids),
                    "afterChildCount": len(children_by_parent[tax_id]),
                    "promotedChildren": promoted_children,
                })
                promoted_this_pass = True
                break

        if not promoted_this_pass:
            break

    return promotions


def write_outputs(
    nodes: dict[int, dict[str, Any]],
    children_by_parent: dict[int, set[int]],
    unresolved: dict[int, int],
    single_leaf_collapses: list[dict[str, Any]],
    single_child_chain_collapses: list[dict[str, Any]],
    sparse_child_promotions: list[dict[str, Any]],
    *,
    input_named_node_count: int,
    pruned_fallback_leaves: list[dict[str, Any]],
    name_source: str,
    name_field: str,
    out_path: Path,
    counts_path: Path,
) -> None:
    output_nodes = sorted(nodes.values(), key=lambda node: (node["depth"], node["id"]))
    child_counts = Counter(len(children_by_parent[node["id"]]) for node in output_nodes)
    rank_counts = Counter(node["rank"] or "(blank)" for node in output_nodes)
    inclusion_counts = Counter("+".join(node["includedBy"]) for node in output_nodes)

    data = {
        "meta": {
            "sourceFile": FULL_TREE_PATH.name,
            "rootTaxId": ROOT_TAX_ID,
            "threshold": THRESHOLD,
            "nameSource": name_source,
            "nameField": name_field,
            "rule": (
                "Start with nodes having the selected display-name field. For nodes with more "
                "than threshold children, repeatedly insert the smallest useful "
                "full-tree ancestor that groups multiple current direct children. "
                "Then collapse common-name nodes with exactly one child and one "
                "leaf descendant by keeping the higher common-name node."
            ),
            "inputNamedNodeCount": input_named_node_count,
            "entryCount": len(output_nodes),
            "intermediaryNodeCount": inclusion_counts["intermediaryMerge"],
            "singleLeafCollapseCount": len(single_leaf_collapses),
            "singleLeafCollapsedNodeCount": sum(
                collapse["removedNodeCount"] for collapse in single_leaf_collapses
            ),
            "singleChildChainCollapseCount": len(single_child_chain_collapses),
            "sparseChildPromotionCount": len(sparse_child_promotions),
            "sparseChildPromotedNodeCount": sum(
                len(promotion["promotedChildren"]) for promotion in sparse_child_promotions
            ),
            "prunedCommonNameFallbackLeafCount": len(pruned_fallback_leaves),
            "unresolvedOverThresholdCount": len(unresolved),
            "unresolvedOverThreshold": [
                {
                    "id": tax_id,
                    "childCount": child_count,
                    "rank": nodes[tax_id]["rank"],
                    "officialName": nodes[tax_id]["officialName"],
                    "displayName": nodes[tax_id]["displayName"],
                }
                for tax_id, child_count in sorted(
                    unresolved.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            ],
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "fields": [
                "id",
                "parentId",
                "ncbiParentId",
                "depth",
                "rank",
                "officialName",
                "commonName",
                "genbankCommonName",
                "displayName",
                "includedBy",
            ],
        },
        "nodes": output_nodes,
    }
    write_json_with_node_lines(out_path, data)

    top_parents = []
    for node in sorted(output_nodes, key=lambda item: len(children_by_parent[item["id"]]), reverse=True)[:50]:
        kids = [nodes[child_id] for child_id in children_by_parent[node["id"]]]
        top_parents.append({
            "childCount": len(kids),
            "id": node["id"],
            "rank": node["rank"] or "(blank)",
            "officialName": node["officialName"],
            "displayName": node["displayName"],
            "childRankCounts": dict(sorted(Counter(child["rank"] or "(blank)" for child in kids).items())),
        })

    counts = {
        "sourceFile": out_path.name,
        "entryCount": len(output_nodes),
        "threshold": THRESHOLD,
        "nameSource": name_source,
        "nameField": name_field,
        "rankCounts": dict(rank_counts.most_common()),
        "inclusionCounts": dict(inclusion_counts.most_common()),
        "prunedCommonNameFallbackLeafCount": len(pruned_fallback_leaves),
        "prunedCommonNameFallbackLeafExamples": pruned_fallback_leaves[:50],
        "singleLeafCollapseCount": len(single_leaf_collapses),
        "singleLeafCollapsedNodeCount": sum(
            collapse["removedNodeCount"] for collapse in single_leaf_collapses
        ),
        "singleLeafCollapseExamples": single_leaf_collapses[:50],
        "singleChildChainCollapseCount": len(single_child_chain_collapses),
        "singleChildChainCollapseExamples": single_child_chain_collapses[:50],
        "sparseChildPromotionCount": len(sparse_child_promotions),
        "sparseChildPromotedNodeCount": sum(
            len(promotion["promotedChildren"]) for promotion in sparse_child_promotions
        ),
        "sparseChildPromotionExamples": sparse_child_promotions[:50],
        "childCountDistribution": {str(key): child_counts[key] for key in sorted(child_counts)},
        "unresolvedOverThreshold": data["meta"]["unresolvedOverThreshold"],
        "topParents": top_parents,
    }
    counts_path.write_text(json.dumps(counts, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_json_with_node_lines(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("{\n")
        handle.write('  "meta": ')
        handle.write(json.dumps(data["meta"], indent=2, ensure_ascii=True))
        handle.write(",\n")
        handle.write('  "nodes": [\n')
        for index, node in enumerate(data["nodes"]):
            suffix = "," if index < len(data["nodes"]) - 1 else ""
            handle.write("    ")
            handle.write(json.dumps(node, ensure_ascii=True, separators=(",", ":")))
            handle.write(suffix + "\n")
        handle.write("  ]\n")
        handle.write("}\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name-source", choices=sorted(NAME_SOURCES), default="genbank")
    args = parser.parse_args()

    source = NAME_SOURCES[args.name_source]
    name_field = str(source["jsonField"])
    out_path = Path(source["outPath"])
    counts_path = Path(source["countsPath"])
    prune_fallback_leaves_before_condense = bool(
        source.get("pruneCommonNameFallbackLeavesBeforeCondense", False)
    )

    parent_by_id, depth_by_id, info_by_id = load_full_tree()
    if name_field == "commonName":
        named_ids = {tax_id for tax_id, info in info_by_id.items() if info[2]}
    elif name_field == "genbankCommonNameOrCommonName":
        named_ids = {tax_id for tax_id, info in info_by_id.items() if info[3] or info[2]}
    else:
        named_ids = {tax_id for tax_id, info in info_by_id.items() if info[3]}
    nodes, children_by_parent = build_common_name_tree(
        parent_by_id,
        depth_by_id,
        info_by_id,
        named_ids,
        name_field,
        str(source["includedBy"]),
    )
    pruned_fallback_leaves: list[dict[str, Any]] = []
    if prune_fallback_leaves_before_condense:
        pruned_fallback_leaves = prune_common_name_fallback_leaves(nodes, children_by_parent)
    sparse_child_promotions = promote_grandchildren_of_sparse_nodes(nodes, children_by_parent)
    unresolved = condense_tree(
        nodes,
        children_by_parent,
        parent_by_id,
        depth_by_id,
        info_by_id,
        name_field,
    )
    single_leaf_collapses = collapse_single_leaf_descendants(nodes, children_by_parent)
    single_child_chain_collapses = collapse_single_child_chains(nodes, children_by_parent)
    unresolved = {
        tax_id: len(children_by_parent[tax_id])
        for tax_id in nodes
        if len(children_by_parent[tax_id]) > THRESHOLD
    }
    write_outputs(
        nodes,
        children_by_parent,
        unresolved,
        single_leaf_collapses,
        single_child_chain_collapses,
        sparse_child_promotions,
        input_named_node_count=len(named_ids),
        pruned_fallback_leaves=pruned_fallback_leaves,
        name_source=args.name_source,
        name_field=name_field,
        out_path=out_path,
        counts_path=counts_path,
    )
    print(f"Wrote {len(nodes)} nodes to {out_path}")
    print(f"Wrote counts to {counts_path}")
    if pruned_fallback_leaves:
        print(f"Pruned {len(pruned_fallback_leaves)} common-name fallback leaves")
    print(f"Collapsed {len(single_leaf_collapses)} one-child, one-leaf branches")
    print(f"Collapsed {len(single_child_chain_collapses)} one-child branching chains")
    print(f"Promoted grandchildren through {len(sparse_child_promotions)} sparse nodes")
    if unresolved:
        print(f"Unresolved overloaded nodes: {len(unresolved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
