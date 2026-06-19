"""Shared helpers for global sandbox rule evaluators."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES = REPO_ROOT / "fixtures"


@dataclass
class RuleInput:
    user_prompt: str
    params: dict[str, Any]
    allowed_chain_ids: list


@dataclass
class RuleOutput:
    recommended_template: str
    recommended_language: str
    audit_hints: list[str]
    compliance_passed: bool
    rejection_reason: str | None = None


def reject_mainnet(inp: RuleInput) -> RuleOutput | None:
    if inp.params.get("target_network") == "mainnet":
        return RuleOutput(
            recommended_template="",
            recommended_language="",
            audit_hints=[],
            compliance_passed=False,
            rejection_reason="mainnet forbidden",
        )
    blocked = {1, 56, 137, 42161, 10, 8453}
    for cid in inp.allowed_chain_ids:
        if isinstance(cid, int) and cid in blocked:
            return RuleOutput(
                recommended_template="",
                recommended_language="",
                audit_hints=[],
                compliance_passed=False,
                rejection_reason=f"mainnet chainId {cid} blocked",
            )
    return None


def load_json_fixture(name: str) -> dict:
    with (FIXTURES / name).open(encoding="utf-8") as f:
        return json.load(f)


def load_yaml_fixture(name: str) -> dict:
    with (FIXTURES / name).open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def ok_result(template: str, language: str, hints: list[str]) -> RuleOutput:
    return RuleOutput(
        recommended_template=template,
        recommended_language=language,
        audit_hints=hints,
        compliance_passed=True,
    )
