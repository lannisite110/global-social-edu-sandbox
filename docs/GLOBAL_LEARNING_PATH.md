# 海外规则沙箱 · 完整学习路径

> **子库** `global-social-edu-sandbox` v0.4.0 · 主库 ≥ v1.0.0 · **5 插件**  
> **Namespace**: `ns-domain-global` · **链**: Fabric 沙箱 `fabric-local`  
> 交叉引用：主库 [LEARNING_PATH.md](../web3-edu-platform-core/docs/LEARNING_PATH.md) **阶段 3D**

---

## 路线总览（约 1–2 周业余 / 4 天全职）

```text
regulatory（监管规则沙箱 · 入口）
    → election（选举哈希共识）
    → welfare（福利反欺诈）
    → logistics（物流审计链）
    → religion（宗教规则表达式沙箱）
```

五插件共用 `ns-domain-global` 教学通道，静态 fixture 匹配 — 无 live OFAC/MiCA/宗教 API。

---

## 第 0 步：环境与注册（所有 Lab 共用）

```bash
cd ~/web3home/web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
make run-rule-engine & make run-scheduler & make run-gateway &
cd frontend-web && npm run dev
# → http://127.0.0.1:5173
```

详见 [QUICK_DEPLOY.md](QUICK_DEPLOY.md) 与主库 [QUICK_DEPLOY.md](../web3-edu-platform-core/docs/QUICK_DEPLOY.md)。

---

## 第 1 步：监管规则沙箱（必做 · 1 天）

| 项 | 内容 |
|----|------|
| 插件 | `edu.global.sandbox.regulatory` |
| 教程 | [tutorials/regulatory-sandbox-intro.md](tutorials/regulatory-sandbox-intro.md) |
| TaskType | `GLOBAL_REGULATORY_RULE_SANDBOX` |
| UI | OFAC/MiCA 静态 fixture 匹配 · eval-card |
| 数据 | `fixtures/ofac-sample.json` · `fixtures/mica-rules-sample.yaml` |

**自检**：输入虚构实体 `Edu Sandbox Entity` → `ofac_match=yes` → 合规拒绝（课堂演示）。

---

## 第 2 步：选举哈希共识（1 天）

| 项 | 内容 |
|----|------|
| 插件 | `edu.global.sandbox.election` |
| 教程 | [tutorials/election-hash-intro.md](tutorials/election-hash-intro.md) |
| TaskType | `GLOBAL_ELECTION_HASH_DEMO` |
| UI | 多节点计票哈希表 · 一致/不一致按钮 |
| 规则 hints | `consensus=true/false` |

**自检**：「验证一致」→ `consensus=true`；「演示不一致」→ `consensus=false`。

---

## 第 3 步：福利反欺诈（1 天）

| 项 | 内容 |
|----|------|
| 插件 | `edu.global.sandbox.welfare` |
| 教程 | [tutorials/welfare-antifraud-intro.md](tutorials/welfare-antifraud-intro.md) |
| TaskType | `GLOBAL_WELFARE_ANTIFRAUD_SIM` |
| UI | 申领列表 · 重复检测 · Merkle 根 |
| 规则 hints | `duplicate_claims` · `merkle_root` |

**自检**：添加重复 claim_id → `duplicate_claims=true` → 合规拒绝。

---

## 第 4 步：物流审计链（1 天）

| 项 | 内容 |
|----|------|
| 插件 | `edu.global.sandbox.logistics` |
| 教程 | [tutorials/logistics-audit-intro.md](tutorials/logistics-audit-intro.md) |
| TaskType | `GLOBAL_LOGISTICS_AUDIT_DEMO` |
| UI | 运单事件链 · 断链演示 |
| 规则 hints | `chain_valid=true/false` |

**自检**：开启「模拟断链」→ `chain_valid=false`。

---

## 第 5 步：宗教规则沙箱（1 天）

| 项 | 内容 |
|----|------|
| 插件 | `edu.global.sandbox.religion` |
| 教程 | [tutorials/religion-rules-intro.md](tutorials/religion-rules-intro.md) |
| TaskType | `GLOBAL_RELIGION_RULE_SANDBOX` |
| UI | Zakat/Waqf 静态表达式 · 金额输入 |
| 数据 | `fixtures/zakat-rules-sample.yaml` |

**自检**：Zakat 金额 8000 → 演示义务计算；低于 nisab → obligation=0。

---

## 教程索引

[docs/tutorials/README.md](tutorials/README.md)

---

## 工程化验收

```bash
cd ~/web3home/global-social-edu-sandbox
make validate && make smoke

cd ../web3-edu-platform-core
make tutorial-audit PLUGINS_DIR=..
make integration-all-plugins
```

分阶段路线：[GLOBAL_PHASES.md](GLOBAL_PHASES.md)

---

## 合规速查

| 禁止 | 替代表述 |
|------|----------|
| live OFAC/MiCA/宗教 API | **静态 fixture** 课堂演示 |
| 真实选举/福利系统对接 | 虚构 Simville · 哈希一致性 Demo |
| 主网 | `fabric-local` only |
| 合规/宗教/金融建议 | 「教学模拟 — not compliance advice」 |

全平台：[COMPLIANCE_MASTER.md](../../COMPLIANCE_MASTER.md)
