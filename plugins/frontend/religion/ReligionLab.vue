<script setup lang="ts">
import { ref } from 'vue'
import { useSimulate } from '../shared/useSimulate'

const PLUGIN_ID = 'edu.global.sandbox.religion'

const ruleType = ref<'zakat' | 'waqf'>('zakat')
const amount = ref(8000)

const { loading, error, result, runSimulate, evaluation } = useSimulate(PLUGIN_ID)

async function run() {
  await runSimulate({ rule_type: ruleType.value, amount: amount.value })
}

const hints = () => (evaluation()?.audit_hints as string[]) ?? []
</script>

<template>
  <section class="card">
    <header class="lab-header">
      <img src="/favicon.png" alt="" width="32" height="32" class="lab-logo" />
      <div>
        <h1>宗教合规规则沙箱</h1>
        <p class="muted">Zakat / Waqf 静态规则表达式 · 非宗教资金清算</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="panel">
        <h2>规则参数</h2>
        <label class="field">
          规则类型
          <select v-model="ruleType">
            <option value="zakat">Zakat（天课）</option>
            <option value="waqf">Waqf（瓦克夫）</option>
          </select>
        </label>
        <label class="field">
          演示金额
          <input v-model.number="amount" type="number" min="0" step="100" />
        </label>
        <button class="primary" :disabled="loading" @click="run">
          {{ loading ? '求值中…' : '求值规则表达式' }}
        </button>
      </div>

      <div class="panel">
        <h2>求值结果</h2>
        <p v-if="!result" class="muted">输入金额后求值，查看虚构阈值与义务/资格判定。</p>
        <ul v-else class="hint-list">
          <li v-for="h in hints()" :key="h">{{ h }}</li>
        </ul>
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
select, input[type="number"] {
  display: block; width: 100%; margin-top: 6px;
  background: #151b23; border: 1px solid #243044; color: inherit;
  border-radius: 8px; padding: 8px;
}
.hint-list { margin: 0; padding-left: 18px; font-size: 13px; color: #c5d0de; }
</style>
