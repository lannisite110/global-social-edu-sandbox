# 任务书 · global-social-edu-sandbox

> **仓库**: `global-social-edu-sandbox`  
> **compliance_tier**: `global_sandbox`  
> **Namespace**: `ns-domain-global`

---

## 1. 目标

5 个**海外社会治理概念仿真**模块（虚构国家/城市/数据，不连接真实系统）。

| # | 模块 | plugin_id | TaskType |
|---|------|-----------|----------|
| 1 | 选举计票哈希演示 | `edu.global.sandbox.election` | `GLOBAL_ELECTION_HASH_DEMO` |
| 2 | 宗教合规规则沙箱 | `edu.global.sandbox.religion` | `GLOBAL_RELIGION_RULE_SANDBOX` |
| 3 | 民生救助防重复 | `edu.global.sandbox.welfare` | `GLOBAL_WELFARE_ANTIFRAUD_SIM` |
| 4 | 金融监管规则沙箱 | `edu.global.sandbox.regulatory` | `GLOBAL_REGULATORY_RULE_SANDBOX` |
| 5 | 后勤审计存证演示 | `edu.global.sandbox.logistics` | `GLOBAL_LOGISTICS_AUDIT_DEMO` |

---

## 2. 模块说明（合规版）

### election
- 演示：多节点提交计票结果哈希 → 比对一致性
- 禁止：真实选票系统、国家大选全线上投票、选民 PII

### religion
- 演示：Zakat/Waqf **规则表达式**求值（静态样例）
- 禁止：真实宗教资金清算、Halal 认证产品

### welfare
- 演示：救助领取 Merkle 防双花算法
- 禁止：联合国/NGO 真实 API、真实难民数据

### regulatory
- 演示：MiCA/OFAC **静态样例名单**规则匹配（JSON fixture）
- 禁止：稳定币支付、跨境汇款产品、RWA 发行、KYC 生产 API

### logistics
- 演示：军费/物资流水哈希链**数据结构**（虚构科目）
- 禁止：真实国防数据、装备参数、涉密后勤系统

---

## 3. 目录

```
global-social-edu-sandbox/
├── plugins/election/
├── plugins/religion/
├── plugins/welfare/
├── plugins/regulatory/
├── plugins/logistics/
├── k8s/overlays/ns-domain-global/
├── fixtures/                    # 静态样例：ofac-sample.json, mica-rules-sample.yaml
└── docs/tutorials/
```

---

## 4. 禁止词（CI 必过）

`stablecoin payment`, `remittance`, `RWA issuance`, `national election`, `online voting production`, `defense classified`, `weapon`

---

## 5. regulatory 模块 rules 示例

```python
def evaluate(inp: RuleInput) -> RuleOutput:
    # 仅加载 fixtures/ofac-sample.json 做字符串匹配演示
    ...
```

不得调用真实 OFAC/MiCA API。

---

## 6. 验收

```bash
cd ../web3-edu-platform-core
for m in ../global-social-edu-sandbox/plugins/*/plugin.manifest.yaml; do
  make validate-plugin MANIFEST="$m"
done
bash ci/compliance/compliance-check.sh ../global-social-edu-sandbox
```

---

## 7. v0.2.0 发布

| 项 | 内容 |
|----|------|
| 版本 | **0.2.0**（见 `VERSION`） |
| 主库依赖 | `web3-edu-platform-core` **≥ v0.3.0** |
| manifest | 5 个插件 `metadata.version: 0.2.0`，`spec.coreVersion: ">=0.3.0 <0.4.0"` |
| 文档 | `CHANGELOG.md`、教程合规页脚 |

验收：

```bash
cd ../web3-edu-platform-core
for m in ../global-social-edu-sandbox/plugins/*/plugin.manifest.yaml; do
  make validate-plugin MANIFEST="$m"
done
bash ci/compliance/compliance-check.sh ../global-social-edu-sandbox
git tag v0.2.0
```
