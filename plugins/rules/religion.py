"""Religion compliance rule sandbox — static Zakat/Waqf expression evaluation."""

from __future__ import annotations

from plugins.rules._common import RuleInput, RuleOutput, load_yaml_fixture, ok_result, reject_mainnet


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    cfg = load_yaml_fixture("zakat-rules-sample.yaml")
    rule_type = str(inp.params.get("rule_type", "zakat")).lower()
    amount = float(inp.params.get("amount", 0))

    if rule_type not in cfg["rules"]:
        return RuleOutput(
            recommended_template="fixtures/zakat-rules-sample.yaml",
            recommended_language="fabric",
            audit_hints=[],
            compliance_passed=False,
            rejection_reason=f"unknown rule_type: {rule_type}",
        )

    rule = cfg["rules"][rule_type]
    if rule_type == "zakat":
        owed = max(0.0, (amount - rule["nisab_threshold"]) * rule["rate"])
        hints = [
            f"rule=zakat",
            f"amount={amount}",
            f"nisab={rule['nisab_threshold']}",
            f"demo_obligation={owed:.2f}",
            "static expression only — not religious or financial advice",
        ]
    else:
        eligible = amount >= rule["min_endowment"]
        hints = [
            f"rule=waqf",
            f"amount={amount}",
            f"min_endowment={rule['min_endowment']}",
            f"eligible={'yes' if eligible else 'no'}",
            "static expression only — not religious or financial advice",
        ]

    return ok_result("fixtures/zakat-rules-sample.yaml", "fabric", hints)
