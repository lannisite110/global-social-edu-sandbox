<p align="center">
  <img src="assets/icon.png" alt="Web3 Education Platform" width="128"/>
</p>

# Global Social Education Sandbox

**v0.4.0** · 海外规则沙箱**概念仿真**教学插件包（子库4）· 主库 LEARNING_PATH **阶段 3D**

选举哈希 / 监管规则 / 福利反欺诈 / 物流审计 / 宗教规则表达式 — **非**金融产品、**非**真实选举、**非**涉密国防。

## 文档

- [完整学习路径](docs/GLOBAL_LEARNING_PATH.md) · [教程索引](docs/tutorials/README.md)
- [学习路径（子库入口）](docs/LEARNING_PATH.md) · [快速部署](docs/QUICK_DEPLOY.md)
- [分阶段工程路线](docs/GLOBAL_PHASES.md)

依赖 [web3-edu-platform-core](https://github.com/lannisite110/web3-edu-platform-core) **v1.1.0**。

变更记录：[CHANGELOG.md](CHANGELOG.md) · 任务书：[TASK.md](TASK.md)

## 插件清单（5）

| 模块 | plugin_id | TaskType |
|------|-----------|----------|
| 监管规则沙箱 | `edu.global.sandbox.regulatory` | `GLOBAL_REGULATORY_RULE_SANDBOX` |
| 选举哈希共识 | `edu.global.sandbox.election` | `GLOBAL_ELECTION_HASH_DEMO` |
| 福利反欺诈 | `edu.global.sandbox.welfare` | `GLOBAL_WELFARE_ANTIFRAUD_SIM` |
| 物流审计链 | `edu.global.sandbox.logistics` | `GLOBAL_LOGISTICS_AUDIT_DEMO` |
| 宗教规则沙箱 | `edu.global.sandbox.religion` | `GLOBAL_RELIGION_RULE_SANDBOX` |

## 快速开始

```bash
make validate && make smoke
bash scripts/joint-debug-smoke.sh   # 需主库后端栈
```

主库联调：

```bash
cd ../web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
make run-rule-engine & make run-scheduler & make run-gateway &
cd frontend-web && npm run dev   # :5173 → 侧边栏「海外沙箱」
```

License: PolyForm Noncommercial 1.0.0
