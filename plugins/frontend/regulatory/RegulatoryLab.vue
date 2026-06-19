<script setup lang="ts">
import { ref } from 'vue'
import { useSimulate } from '../shared/useSimulate'

const PLUGIN_ID = 'edu.global.sandbox.regulatory'

const entityName = ref('')
const micaPattern = ref('')
const sampleEntities = ['Fictional Trade Corp', 'Edu Sandbox Entity', 'Unknown Corp']
const micaPatterns = [
  { value: '', label: '（不检查 MiCA）' },
  { value: 'whitepaper-missing', label: 'whitepaper-missing' },
  { value: 'asset-referenced', label: 'asset-referenced' },
  { value: 'unlicensed-custodian', label: 'unlicensed-custodian' },
]

const { loading, error, result, runSimulate, evaluation } = useSimulate(PLUGIN_ID)

async function run() {
  await runSimulate({
    entity_name: entityName.value,
    mica_pattern: micaPattern.value || undefined,
  }, entityName.value)
}

const hints = () => (evaluation()?.audit_hints as string[]) ?? []
</script>

<template>
  <section class="card">
    <header class="lab-header">
      <img src="/favicon.png" alt="" width="32" height="32" class="lab-logo" />
      <div>
        <h1>金融监管规则沙箱</h1>
        <p class="muted">静态 OFAC/MiCA 样例名单 · 无真实 API · 非合规建议</p>
      </div>
    </header>

    <div class="lab-grid">
      <div class="panel">
        <h2>规则匹配</h2>
        <label class="field">
          实体名称
          <input v-model="entityName" placeholder="输入虚构实体名称" />
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
          MiCA 演示规则
          <select v-model="micaPattern">
            <option v-for="p in micaPatterns" :key="p.value" :value="p.value">{{ p.label }}</option>
          </select>
        </label>
        <button class="primary" :disabled="loading" @click="run">
          {{ loading ? '匹配中…' : '运行静态规则匹配' }}
        </button>
      </div>

      <div class="panel">
        <h2>匹配结果</h2>
        <p v-if="!result" class="muted">选择样例实体或输入名称，对照 fixtures 静态名单。</p>
        <ul v-else class="hint-list">
          <li v-for="h in hints()" :key="h">{{ h }}</li>
        </ul>
        <p v-if="evaluation()" :class="evaluation()?.compliance_passed ? 'ok' : 'warn'">
          {{ evaluation()?.compliance_passed ? '✓ 未命中拒绝规则' : '⚠ ' + (evaluation()?.rejection_reason || '课堂复核') }}
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
</style>
