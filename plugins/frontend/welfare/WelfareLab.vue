<script setup lang="ts">
import { ref } from 'vue'
import { useSimulate } from '../shared/useSimulate'

const PLUGIN_ID = 'edu.global.sandbox.welfare'

const claims = ref([
  { claim_id: 'SIM-CLM-001', amount: 200, region: 'NorthDemo' },
  { claim_id: 'SIM-CLM-002', amount: 150, region: 'SouthDemo' },
  { claim_id: 'SIM-CLM-003', amount: 300, region: 'EastDemo' },
])
const verifyClaimId = ref('SIM-CLM-001')
const injectDuplicate = ref(false)

const { loading, error, result, runSimulate, evaluation } = useSimulate(PLUGIN_ID)

async function run() {
  const batch = injectDuplicate.value
    ? [...claims.value, { claim_id: 'SIM-CLM-001', amount: 200, region: 'NorthDemo' }]
    : claims.value
  await runSimulate({ claims: batch, verify_claim_id: verifyClaimId.value })
}

const hints = () => (evaluation()?.audit_hints as string[]) ?? []
</script>

<template>
  <section class="card">
    <header class="lab-header">
      <img src="/favicon.png" alt="" width="32" height="32" class="lab-logo" />
      <div>
        <h1>民生救助防重复</h1>
        <p class="muted">Merkle 防双花算法 · 虚构受益人 ID · 非真实 NGO 数据</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="panel">
        <h2>救助申领批次</h2>
        <table class="data-table">
          <thead>
            <tr><th>申领 ID</th><th>金额</th><th>区域</th></tr>
          </thead>
          <tbody>
            <tr v-for="c in claims" :key="c.claim_id">
              <td>{{ c.claim_id }}</td>
              <td>{{ c.amount }}</td>
              <td>{{ c.region }}</td>
            </tr>
          </tbody>
        </table>
        <label class="field">
          验证申领 ID
          <select v-model="verifyClaimId">
            <option v-for="c in claims" :key="c.claim_id" :value="c.claim_id">{{ c.claim_id }}</option>
          </select>
        </label>
        <label class="checkbox">
          <input v-model="injectDuplicate" type="checkbox" />
          注入重复 claim_id（演示防欺诈）
        </label>
        <button class="primary" :disabled="loading" @click="run">
          {{ loading ? '验证中…' : '构建 Merkle 并验证' }}
        </button>
      </div>

      <div class="panel">
        <h2>Merkle 验证</h2>
        <p v-if="!result" class="muted">提交后显示 Merkle 根与重复检测结果。</p>
        <ul v-else class="hint-list">
          <li v-for="h in hints()" :key="h">{{ h }}</li>
        </ul>
        <p v-if="evaluation()" :class="evaluation()?.compliance_passed ? 'ok' : 'warn'">
          {{ evaluation()?.compliance_passed ? '✓ 批次有效' : '✗ ' + (evaluation()?.rejection_reason || '检测到异常') }}
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
select { display: block; width: 100%; margin-top: 6px; background: #151b23; border: 1px solid #243044; color: inherit; border-radius: 8px; padding: 8px; }
.checkbox { display: flex; align-items: center; gap: 8px; margin: 12px 0; font-size: 13px; }
.hint-list { margin: 0; padding-left: 18px; font-size: 13px; color: #c5d0de; }
.ok { color: #6ee7b7; font-weight: 600; }
.warn { color: #fbbf24; font-weight: 600; }
</style>
