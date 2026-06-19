"""Welfare anti-fraud simulation — Merkle proof and duplicate claim detection."""

from __future__ import annotations

import hashlib
from typing import Any

from plugins.rules._common import RuleInput, RuleOutput, load_json_fixture, ok_result, reject_mainnet


def _leaf_hash(claim_id: str) -> str:
    return hashlib.sha256(claim_id.encode()).hexdigest()


def _build_merkle_root(leaves: list[str]) -> str:
    if not leaves:
        return ""
    layer = leaves[:]
    while len(layer) > 1:
        if len(layer) % 2 == 1:
            layer.append(layer[-1])
        layer = [
            hashlib.sha256((layer[i] + layer[i + 1]).encode()).hexdigest()
            for i in range(0, len(layer), 2)
        ]
    return layer[0]


def evaluate(inp: RuleInput) -> RuleOutput:
    blocked = reject_mainnet(inp)
    if blocked:
        return blocked

    fixture = load_json_fixture("welfare-claims-sample.json")
    claims: list[dict[str, Any]] = inp.params.get("claims") or fixture["claims"]
    claim_ids = [c["claim_id"] for c in claims]
    duplicates = len(claim_ids) != len(set(claim_ids))

    leaves = sorted(_leaf_hash(cid) for cid in claim_ids)
    root = _build_merkle_root(leaves)

    verify_id = inp.params.get("verify_claim_id")
    proof_ok = None
    if verify_id:
        proof_ok = verify_id in claim_ids and not duplicates

    hints = [
        f"claim_count={len(claims)}",
        f"merkle_root={root[:16]}...",
        f"duplicate_detected={'yes' if duplicates else 'no'}",
        "fictional beneficiary IDs only",
        "fabric-local sandbox",
    ]
    if verify_id:
        hints.append(f"verify_claim_id={verify_id}")
        hints.append(f"proof_valid={'yes' if proof_ok else 'no'}")

    if duplicates:
        return RuleOutput(
            recommended_template="fixtures/welfare-claims-sample.json",
            recommended_language="fabric",
            audit_hints=hints,
            compliance_passed=False,
            rejection_reason="duplicate claim_id detected in demo batch",
        )
    return ok_result("fixtures/welfare-claims-sample.json", "fabric", hints)
