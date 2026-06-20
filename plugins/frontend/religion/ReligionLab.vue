<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../shared/useLabSimulate'
import { parseHints } from '../shared/parseHints'

const PLUGIN_ID = 'edu.global.sandbox.religion'
const TASK_TYPE = 'GLOBAL_RELIGION_RULE_SANDBOX'

const { t } = useLabI18n(PLUGIN_ID)

const ruleType = ref<'zakat' | 'waqf'>('zakat')
const amount = ref(8000)

const ruleTypeOptions = computed(() => [
  { value: 'zakat' as const, label: t('rule_zakat') },
  { value: 'waqf' as const, label: t('rule_waqf') },
])

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
        <h1>{{ t('title') }}</h1>
        <p class="muted">{{ t('subtitle') }}</p>
      </div>
    </header>

    <div v-if="evaluation" class="eval-card">
      <p class="ok">{{ t('evalLine', { rule: hints.rule, amount: hints.amount }) }}</p>
      <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
    </div>

    <div class="lab-grid">
      <div class="panel">
        <h2>{{ t('ruleParams') }}</h2>
        <label class="field">
          {{ t('ruleType') }}
          <select v-model="ruleType">
            <option v-for="opt in ruleTypeOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
        </label>
        <label class="field">
          {{ t('demoAmount') }}
          <input v-model.number="amount" type="number" min="0" step="100" />
        </label>
        <button class="primary" :disabled="loading" @click="run">
          {{ loading ? t('evaluating') : t('evalRule') }}
        </button>
      </div>

      <div class="panel">
        <h2>{{ t('resultSection') }}</h2>
        <p v-if="!evaluation" class="muted">{{ t('resultHint') }}</p>
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
