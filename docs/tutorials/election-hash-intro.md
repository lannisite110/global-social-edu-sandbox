# Election Hash Consensus Demo

**Module**: `edu.global.sandbox.election`  
**TaskType**: `GLOBAL_ELECTION_HASH_DEMO`

## Purpose

Demonstrate how multiple fictional tally nodes submit result hashes and how a classroom sandbox checks hash consensus — **not** a real voting system.

## Parameters

| Field | Description |
|-------|-------------|
| `nodes` | Optional list of `{node_id, tally_hash}`; defaults to `fixtures/election-nodes-sample.json` |

## Compliance

- Fictional city/jurisdiction only
- No voter PII, no production voting integration
- Runs in `ns-domain-global` / `fabric-local`

## API

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.global.sandbox.election/simulate \
  -H 'Content-Type: application/json' \
  -d '{"params":{},"allowed_chain_ids":["fabric-local"]}'
```

---

> **Compliance footer** · `compliance_tier: global_sandbox` · fictional jurisdictions and data only · `fabric-local` sandbox only · no real elections, religious fund settlement, NGO/live regulatory APIs, stablecoin/remittance/RWA, or classified defense systems · classroom simulation only — not legal or compliance advice
