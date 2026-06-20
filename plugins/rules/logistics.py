"""Logistics audit demo — fictional supply ledger hash chain verification."""

from __future__ import annotations

import hashlib
from typing import Any

from plugins.rules._common import RuleInput, RuleOutput, ok_result, reject_mainnet


def _block_hash(prev: str, entry: dict[str, Any]) -> str:
    payload = f"{prev}|{entry.get('account', '')}|{entry.get('amount', 0)}|{entry.get('memo', '')}"
    return hashlib.sha256(payload.encode()).hexdigest()


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    default_entries = [
        {"account": "DEMO-SUPPLY-01", "amount": 100, "memo": "fictional rations batch A"},
        {"account": "DEMO-SUPPLY-02", "amount": 50, "memo": "fictional medical kits"},
        {"account": "DEMO-SUPPLY-03", "amount": 75, "memo": "fictional shelter materials"},
    ]
    entries: list[dict[str, Any]] = inp.params.get("entries") or default_entries

    chain: list[str] = []
    prev = "0" * 64
    for entry in entries:
        h = _block_hash(prev, entry)
        chain.append(h)
        prev = h

    expected_tail = inp.params.get("expected_tail_hash")
    tail_ok = expected_tail is None or chain[-1] == expected_tail

    hints = [
        f"entry_count={len(entries)}",
        f"chain_head={chain[0][:16]}...",
        f"chain_tail={chain[-1][:16]}...",
        f"chain_valid={'true' if tail_ok else 'false'}",
        "fictional accounts only — not classified logistics data",
        "fabric-local sandbox",
    ]

    if not tail_ok:
        return RuleOutput(
            recommended_template="docs/tutorials/logistics-audit-intro.md",
            recommended_language="fabric",
            audit_hints=hints,
            compliance_passed=False,
            rejection_reason="hash chain tail mismatch in demo ledger",
        )
    return ok_result("docs/tutorials/logistics-audit-intro.md", "fabric", hints)
