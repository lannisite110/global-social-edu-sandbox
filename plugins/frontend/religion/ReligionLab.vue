<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabSimulate } from '../shared/useLabSimulate'
import { parseHints } from '../shared/parseHints'

const PLUGIN_ID = 'edu.global.sandbox.religion'
const TASK_TYPE = 'GLOBAL_RELIGION_RULE_SANDBOX'

const ruleType = ref<'zakat' | 'waqf'>('zakat')
const amount = ref(8000)

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

function run() {
  runSimulate(
    'Zakat/Waqf 规则表达式求值',
    { rule_type: ruleType.value, amount: amount.value },
    { taskType: TASK_TYPE },
  )
}
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

    <div v-if="evaluation" class="eval-card">
      <p class="ok">✓ 规则 {{ hints.rule }} · 金额 {{ hints.amount }}</p>
      <p v-if="taskStatus" class="status">任务: {{ taskStatus }}</p>
    </div>

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
        <p v-if="!evaluation" class="muted">输入金额后求值，查看虚构阈值与义务/资格判定。</p>
        <ul v-else class="hint-list">
          <li v-for="(v, k) in hints" :key="k">{{ k }}={{ v }}</li>
        </ul>
      </div>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
    <pre v-if="taskReport" class="result">{{ JSON.stringify(taskReport, null, 2) }}</pre>
    <pre v-else-if="result" class="result">{{ JSON.stringify(result, null, 2) }}</pre>
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
.eval-card { background: #0d2818; border: 1px solid #166534; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
.ok { color: #6ee7b7; font-weight: 600; margin: 0; }
.status { color: #9ec5ff; font-size: 12px; margin-top: 6px; }
</style>
