# Welfare Anti-Fraud Simulation

**Module**: `edu.global.sandbox.welfare`  
**TaskType**: `GLOBAL_WELFARE_ANTIFRAUD_SIM`

## Purpose

Build a Merkle root over fictional aid claims and detect duplicate `claim_id` values — a classroom anti double-claim algorithm demo.

## Parameters

| Field | Description |
|-------|-------------|
| `claims` | Optional claim list; defaults to `fixtures/welfare-claims-sample.json` |
| `verify_claim_id` | Optional claim ID to verify membership |

## Compliance

- Fictional beneficiary IDs only (no real refugee or NGO data)
- No United Nations or NGO live API integration
- `fabric-local` sandbox

## API

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.global.sandbox.welfare/simulate \
  -H 'Content-Type: application/json' \
  -d '{"params":{"verify_claim_id":"SIM-CLM-002"},"allowed_chain_ids":["fabric-local"]}'
```

---

> **Compliance footer** · `compliance_tier: global_sandbox` · fictional jurisdictions and data only · `fabric-local` sandbox only · no real elections, religious fund settlement, NGO/live regulatory APIs, stablecoin/remittance/RWA, or classified defense systems · classroom simulation only — not legal or compliance advice
