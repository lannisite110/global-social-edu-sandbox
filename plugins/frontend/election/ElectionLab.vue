<script setup lang="ts">
import { computed, ref } from 'vue'
import { useLabSimulate } from '../shared/useLabSimulate'
import { parseHints, hintBool } from '../shared/parseHints'

const PLUGIN_ID = 'edu.global.sandbox.election'
const TASK_TYPE = 'GLOBAL_ELECTION_HASH_DEMO'

const nodes = ref([
  { node_id: 'node-alpha', tally_hash: 'a3f5c8e2b1d94f6078e5a2c3b4d5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f7' },
  { node_id: 'node-beta', tally_hash: 'a3f5c8e2b1d94f6078e5a2c3b4d5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f7' },
  { node_id: 'node-gamma', tally_hash: 'a3f5c8e2b1d94f6078e5a2c3b4d5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f7' },
])

const CONSENSUS_HASH = 'a3f5c8e2b1d94f6078e5a2c3b4d5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f7'
const { loading, error, result, taskStatus, taskReport, runSimulate, parseEvaluation } =
  useLabSimulate(PLUGIN_ID)

const evaluation = computed(() => parseEvaluation(result.value?.evaluation))
const hints = computed(() => parseHints(evaluation.value?.audit_hints))
const consensus = computed(() => hintBool(hints.value, 'consensus'))

function run(consensusMode: boolean) {
  const batch = nodes.value.map((n, i) => ({
    ...n,
    tally_hash: consensusMode || i < 2 ? CONSENSUS_HASH : 'ffff0000deadbeef' + CONSENSUS_HASH.slice(16),
  }))
  runSimulate('选举计票哈希一致性演示', { nodes: batch }, { taskType: TASK_TYPE })
}
</script>

<template>
  <section class="card">
    <header class="lab-header">
      <img src="/favicon.png" alt="" width="32" height="32" class="lab-logo" />
      <div>
        <h1>选举计票哈希演示</h1>
        <p class="muted">虚构城市 Simville · 多节点哈希一致性 · 非真实投票系统</p>
      </div>
    </header>

    <div v-if="evaluation" class="eval-card">
      <p class="ok">✓ 规则评估 · 节点 {{ hints.node_count }} · 共识 {{ consensus ? '达成' : '未达成' }}</p>
      <p v-if="taskStatus" class="status">任务: {{ taskStatus }}</p>
    </div>

    <div class="lab-grid">
      <div class="panel">
        <h2>计票节点</h2>
        <table class="data-table">
          <thead>
            <tr><th>节点</th><th>计票哈希（截断）</th></tr>
          </thead>
          <tbody>
            <tr v-for="n in nodes" :key="n.node_id">
              <td>{{ n.node_id }}</td>
              <td><code>{{ n.tally_hash.slice(0, 20) }}…</code></td>
            </tr>
          </tbody>
        </table>
        <div class="actions">
          <button class="primary" :disabled="loading" @click="run(true)">
            {{ loading ? '比对中…' : '验证一致' }}
          </button>
          <button class="secondary" :disabled="loading" @click="run(false)">
            演示不一致
          </button>
        </div>
      </div>

      <div class="panel">
        <h2>共识状态</h2>
        <p v-if="!evaluation && !error" class="muted">点击按钮提交仿真实验，查看哈希是否一致。</p>
        <ul v-if="evaluation" class="hint-list">
          <li v-for="(v, k) in hints" :key="k">{{ k }}={{ v }}</li>
        </ul>
        <p v-if="evaluation" :class="consensus ? 'ok' : 'warn'">
          {{ consensus ? '✓ 共识达成' : '✗ 哈希不一致（教学演示）' }}
        </p>
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
.data-table { width: 100%; font-size: 12px; border-collapse: collapse; }
.data-table th, .data-table td { text-align: left; padding: 6px 8px; border-bottom: 1px solid #243044; }
code { color: #6ee7b7; font-size: 11px; }
.hint-list { margin: 0; padding-left: 18px; font-size: 13px; color: #c5d0de; }
.actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.secondary {
  background: #1e2733; color: #c5d0de; border: 1px solid #243044;
  padding: 10px 16px; border-radius: 8px; cursor: pointer;
}
.secondary:disabled { opacity: 0.6; cursor: not-allowed; }
.ok { color: #6ee7b7; font-weight: 600; }
.warn { color: #fbbf24; font-weight: 600; }
.eval-card { background: #0d2818; border: 1px solid #166534; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
.status { color: #9ec5ff; font-size: 12px; margin-top: 6px; }
</style>
