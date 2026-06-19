<p align="center">
  <img src="assets/icon.png" alt="Web3 Education Platform" width="128"/>
</p>

# Global Social Education Sandbox

海外社会治理**概念仿真**教学插件包（子库4）。

- 选举哈希 / 宗教规则 / 民生防欺诈 / 监管规则沙箱 / 后勤存证
- **非**金融产品、**非**真实选举、**非**涉密国防

见 [AGENT_TASK.md](AGENT_TASK.md)。

## 本地联调

```bash
cd ../web3-edu-platform-core
make register-plugins PLUGINS_DIR=..
# 三终端：make run-rule-engine / run-scheduler / run-gateway
cd frontend-web && npm run dev   # :5173 → 侧边栏「海外沙箱」
```

License: PolyForm Noncommercial 1.0.0
