# 海外规则沙箱子库 · 分阶段路线图

> **仓库**: `global-social-edu-sandbox` · **v0.4.0**  
> **插件**: 5 · **Namespace**: `ns-domain-global` · **chainId**: `fabric-local`  
> **参照**: [enterprise-gov-edu-demo/docs/GOV_PHASES.md](../enterprise-gov-edu-demo/docs/GOV_PHASES.md)

---

## Phase 0 — 共享 composable + Job 审计 ✅

| 任务 | 状态 |
|------|------|
| `useLabSimulate` | ✅ `plugins/frontend/shared/`（`useSimulate` 为别名） |
| `parseHints.ts` | ✅ |
| 五 Lab eval-card + taskType | ✅ |
| K8s Job | ✅ 5 个 Job 补全 command 门禁 |
| 规则 hints | ✅ consensus/duplicate/chain_valid 结构化 |
| 验收脚本 | ✅ `scripts/global-phase0-verify.sh` · `scripts/joint-debug-smoke.sh` |

---

## Phase 1 — 总入口文档 ✅

- [GLOBAL_LEARNING_PATH.md](GLOBAL_LEARNING_PATH.md) · [docs/tutorials/README.md](tutorials/README.md) · 主库 **阶段 3D**

---

## Phase 2 — 五 Lab UI 对齐 ✅

- regulatory / election / welfare / logistics / religion — eval-card · taskStatus/taskReport · grid 布局

---

## Phase 3 — 规则/K8s 门禁 ✅

- 五 Job command gate · 规则结构化 hints

---

## Phase 4 — 教程 + v0.4.0 发布 ✅

- manifest **0.4.0** · `CHANGELOG.md` · `VERSION=0.4.0` · tag **v0.4.0**

```bash
cd ~/web3home/global-social-edu-sandbox
make validate && make smoke
```

---

## P0 进度

| 子库 | 状态 |
|------|------|
| hot / trace / gov / **global（本仓）** | ✅ v0.4.0 |
