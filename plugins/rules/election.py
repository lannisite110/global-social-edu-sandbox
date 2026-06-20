"""Election tally hash consensus demo — fictional multi-node hash comparison."""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, load_json_fixture, ok_result, reject_mainnet


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    fixture = load_json_fixture("election-nodes-sample.json")
    nodes = inp.params.get("nodes") or fixture["nodes"]
    hashes = [n.get("tally_hash", "") for n in nodes]
    unique = set(hashes)
    consensus = len(unique) == 1 and all(hashes)

    hints = [
        f"node_count={len(nodes)}",
        f"unique_hashes={len(unique)}",
        f"consensus={'true' if consensus else 'false'}",
        "fabric-local sandbox only",
        "fictional jurisdiction — not a real voting system",
    ]
    if not consensus:
        return RuleOutput(
            recommended_template="fixtures/election-nodes-sample.json",
            recommended_language="fabric",
            audit_hints=hints,
            compliance_passed=False,
            rejection_reason="tally hash mismatch across demo nodes",
        )
    return ok_result("fixtures/election-nodes-sample.json", "fabric", hints)
