<script setup lang="ts">
import { ref } from 'vue'
import { useSimulate } from '../shared/useSimulate'

const PLUGIN_ID = 'edu.global.sandbox.logistics'

const entries = ref([
  { account: 'DEMO-SUPPLY-01', amount: 100, memo: 'fictional rations batch A' },
  { account: 'DEMO-SUPPLY-02', amount: 50, memo: 'fictional medical kits' },
  { account: 'DEMO-SUPPLY-03', amount: 75, memo: 'fictional shelter materials' },
])

const { loading, error, result, runSimulate, evaluation } = useSimulate(PLUGIN_ID)

async function run(valid = true) {
  const batch = valid
    ? entries.value
    : [...entries.value, { account: 'DEMO-TAMPER', amount: 999, memo: 'tampered row demo' }]
  await runSimulate({ entries: batch })
}

const hints = () => (evaluation()?.audit_hints as string[]) ?? []
</script>

<template>
  <section class="card">
    <header class="lab-header">
      <img src="/favicon.png" alt="" width="32" height="32" class="lab-logo" />
      <div>
        <h1>后勤审计存证演示</h1>
        <p class="muted">虚构物资流水哈希链 · 数据结构教学 · 非涉密后勤系统</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="panel">
        <h2>流水账本</h2>
        <table class="data-table">
          <thead>
            <tr><th>科目</th><th>数量</th><th>备注</th></tr>
          </thead>
          <tbody>
            <tr v-for="(e, i) in entries" :key="i">
              <td>{{ e.account }}</td>
              <td>{{ e.amount }}</td>
              <td class="memo">{{ e.memo }}</td>
            </tr>
          </tbody>
        </table>
        <div class="actions">
          <button class="primary" :disabled="loading" @click="run(true)">
            {{ loading ? '计算中…' : '验证哈希链' }}
          </button>
          <button class="secondary" :disabled="loading" @click="run(false)">
            追加异常行
          </button>
        </div>
      </div>

      <div class="panel">
        <h2>链完整性</h2>
        <p v-if="!result" class="muted">每条流水与前序哈希链接，演示链式存证结构。</p>
        <ul v-else class="hint-list">
          <li v-for="h in hints()" :key="h">{{ h }}</li>
        </ul>
        <p v-if="evaluation()" :class="evaluation()?.compliance_passed ? 'ok' : 'warn'">
          {{ evaluation()?.compliance_passed ? '✓ 哈希链有效' : '✗ ' + (evaluation()?.rejection_reason || '链校验失败') }}
        </p>
      </div>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <pre v-if="result" class="result">{{ JSON.stringify(result, null, 2) }}</pre>
  </section>
</template>

<style scoped>
.lab-header { display: flex; gap: 12px; align-items: center; margin-bottom: 16px; }
.lab-logo { border-radius: 6px; }
.lab-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 16px 0; }
.panel { background: #0f1419; border: 1px solid #243044; border-radius: 8px; padding: 14px; }
.panel h2 { margin: 0 0 10px; font-size: 14px; color: #9ec5ff; }
.data-table { width: 100%; font-size: 12px; border-collapse: collapse; margin-bottom: 12px; }
.data-table th, .data-table td { text-align: left; padding: 6px 8px; border-bottom: 1px solid #243044; }
.memo { color: #8b9cb3; font-size: 11px; }
.actions { display: flex; gap: 8px; flex-wrap: wrap; }
.secondary {
  background: #1e2733; color: #c5d0de; border: 1px solid #243044;
  padding: 10px 16px; border-radius: 8px; cursor: pointer;
}
.secondary:disabled { opacity: 0.6; cursor: not-allowed; }
.hint-list { margin: 0; padding-left: 18px; font-size: 13px; color: #c5d0de; }
.ok { color: #6ee7b7; font-weight: 600; }
.warn { color: #fbbf24; font-weight: 600; }
</style>
