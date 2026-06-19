# Regulatory Rule Sandbox

**Module**: `edu.global.sandbox.regulatory`  
**TaskType**: `GLOBAL_REGULATORY_RULE_SANDBOX`

## Purpose

Match entity names against a **static fictional OFAC-style list** and MiCA-style demo rules from local fixtures — no live regulatory API calls.

## Parameters

| Field | Description |
|-------|-------------|
| `entity_name` | Entity string to check against `fixtures/ofac-sample.json` |
| `mica_pattern` | Pattern key from `fixtures/mica-rules-sample.yaml` |

## Compliance

- Static JSON/YAML fixtures only
- No stablecoin payments, cross-border remittance products, or RWA issuance
- No KYC production APIs
- Classroom simulation — not legal or compliance advice

## API

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.global.sandbox.regulatory/simulate \
  -H 'Content-Type: application/json' \
  -d '{"params":{"entity_name":"Edu Sandbox Entity"},"allowed_chain_ids":["fabric-local"]}'
```

---

> **Compliance footer** · `compliance_tier: global_sandbox` · fictional jurisdictions and data only · `fabric-local` sandbox only · no real elections, religious fund settlement, NGO/live regulatory APIs, stablecoin/remittance/RWA, or classified defense systems · classroom simulation only — not legal or compliance advice
