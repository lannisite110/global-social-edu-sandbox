"""Regulatory rule sandbox — static OFAC/MiCA fixture matching (no live APIs)."""

from __future__ import annotations

from plugins.rules._common import (
    RuleInput,
    RuleOutput,
    load_json_fixture,
    load_yaml_fixture,
    ok_result,
    reject_mainnet,
)


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    ofac = load_json_fixture("ofac-sample.json")
    mica = load_yaml_fixture("mica-rules-sample.yaml")

    entity_name = str(
        inp.params.get("entity_name") or inp.user_prompt or ""
    ).strip()
    mica_pattern = str(inp.params.get("mica_pattern", "")).strip()

    ofac_hit = None
    if entity_name:
        for ent in ofac["entities"]:
            if ent["name"].lower() in entity_name.lower() or entity_name.lower() in ent["name"].lower():
                ofac_hit = ent
                break

    mica_hit = None
    if mica_pattern:
        for rule in mica["rules"]:
            if rule["pattern"] == mica_pattern:
                mica_hit = rule
                break

    hints = [
        "static fixture matching only",
        "no live OFAC or MiCA API calls",
        f"ofac_match={'yes' if ofac_hit else 'no'}",
        f"mica_match={'yes' if mica_hit else 'no'}",
        "classroom simulation — not compliance advice",
    ]
    if ofac_hit:
        hints.append(f"matched_entity={ofac_hit['id']}")
    if mica_hit:
        hints.append(f"mica_rule={mica_hit['id']}")

    if ofac_hit or (mica_hit and mica_hit.get("action") == "reject"):
        return RuleOutput(
            recommended_template="fixtures/ofac-sample.json",
            recommended_language="fabric",
            audit_hints=hints,
            compliance_passed=False,
            rejection_reason="demo rule match flagged for classroom review",
        )
    return ok_result("fixtures/ofac-sample.json", "fabric", hints)
