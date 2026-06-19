# Religion Rule Sandbox

**Module**: `edu.global.sandbox.religion`  
**TaskType**: `GLOBAL_RELIGION_RULE_SANDBOX`

## Purpose

Evaluate static Zakat and Waqf **rule expressions** from classroom fixtures — not religious fund settlement or product certification.

## Parameters

| Field | Description |
|-------|-------------|
| `rule_type` | `zakat` or `waqf` |
| `amount` | Numeric demo amount |

## Compliance

- Static YAML rules in `fixtures/zakat-rules-sample.yaml`
- No real religious fund clearing or Halal product certification
- Educational simulation only

## API

```bash
curl -X POST http://127.0.0.1:8080/api/v1/labs/edu.global.sandbox.religion/simulate \
  -H 'Content-Type: application/json' \
  -d '{"params":{"rule_type":"zakat","amount":8000},"allowed_chain_ids":["fabric-local"]}'
```
