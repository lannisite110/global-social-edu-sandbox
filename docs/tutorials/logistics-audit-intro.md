# Logistics Audit Ledger Demo

**Module**: `edu.global.sandbox.logistics`  
**TaskType**: `GLOBAL_LOGISTICS_AUDIT_DEMO`

## Purpose

Demonstrate a hash-linked ledger over **fictional supply accounts** — a data-structure teaching lab, not a classified logistics system.

## Parameters

| Field | Description |
|-------|-------------|
| `entries` | Optional list of `{account, amount, memo}` demo rows |
| `expected_tail_hash` | Optional tail hash for chain verification |

## Compliance

- Fictional account codes and memos only
- No real defense data, equipment parameters, or classified systems
- `ns-domain-global` / `fabric-local`

## API

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.global.sandbox.logistics/simulate \
  -H 'Content-Type: application/json' \
  -d '{"params":{},"allowed_chain_ids":["fabric-local"]}'
```

---

> **Compliance footer** · `compliance_tier: global_sandbox` · fictional jurisdictions and data only · `fabric-local` sandbox only · no real elections, religious fund settlement, NGO/live regulatory APIs, stablecoin/remittance/RWA, or classified defense systems · classroom simulation only — not legal or compliance advice
