<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabI18n } from '@/composables/useLabI18n'
import { useLabSimulate } from '../shared/useLabSimulate'
import { parseHints, hintBool } from '../shared/parseHints'

const PLUGIN_ID = 'edu.global.sandbox.regulatory'
const TASK_TYPE = 'GLOBAL_REGULATORY_RULE_SANDBOX'

const { t } = useLabI18n(PLUGIN_ID)

const entityName = ref('')
const micaPattern = ref('')
const sampleEntities = ['Fictional Trade Corp', 'Edu Sandbox Entity', 'Unknown Corp']
const micaPatterns = computed(() => [
  { value: '', label: t('mica_none') },
  { value: 'whitepaper-missing', label: 'whitepaper-missing' },
  { value: 'asset-referenced', label: 'asset-referenced' },
  { value: 'unlicensed-custodian', label: 'unlicensed-custodian' },
])

const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))

function run() {
  runSimulate(
    entityName.value || 'regulatory rule match',
    {
      entity_name: entityName.value,
      mica_pattern: micaPattern.value || undefined,
    },
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
      <p class="ok">{{ t('evalOfac', { ofac: hints.ofac_match, mica: hints.mica_match }) }}</p>
      <p v-if="taskStatus" class="status">{{ t('task') }}: {{ taskStatus }}</p>
    </div>

    <div class="lab-grid">
      <div class="panel">
        <h2>{{ t('ruleMatch') }}</h2>
        <label class="field">
          {{ t('entityName') }}
          <input v-model="entityName" :placeholder="t('entityPlaceholder')" />
        </label>
        <div class="chips">
          <button
            v-for="e in sampleEntities"
            :key="e"
            type="button"
            class="chip"
            @click="entityName = e"
          >{{ e }}</button>
        </div>
        <label class="field">
          {{ t('micaRule') }}
          <select v-model="micaPattern">
            <option v-for="p in micaPatterns" :key="p.value" :value="p.value">{{ p.label }}</option>
          </select>
        </label>
        <button class="primary" :disabled="loading" @click="run">
          {{ loading ? t('matching') : t('runMatch') }}
        </button>
      </div>

      <div class="panel">
        <h2>{{ t('matchResult') }}</h2>
        <p v-if="!evaluation && !error" class="muted">{{ t('matchHint') }}</p>
        <ul v-if="evaluation" class="hint-list">
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
input, select {
  display: block; width: 100%; margin-top: 6px;
  background: #151b23; border: 1px solid #243044; color: inherit;
  border-radius: 8px; padding: 8px;
}
.chips { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 12px; }
.chip {
  background: #1e2733; border: 1px solid #243044; color: #9ec5ff;
  padding: 4px 10px; border-radius: 6px; font-size: 11px; cursor: pointer;
}
.chip:hover { background: #1a3a5c; }
.hint-list { margin: 0; padding-left: 18px; font-size: 13px; color: #c5d0de; }
.ok { color: #6ee7b7; font-weight: 600; }
.warn { color: #fbbf24; font-weight: 600; }
.eval-card { background: #0d2818; border: 1px solid #166534; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
.status { color: #9ec5ff; font-size: 12px; margin-top: 6px; }
</style>
