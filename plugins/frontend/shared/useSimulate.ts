import { ref } from 'vue'

export function useSimulate(pluginId: string, defaultChainIds: (number | string)[] = ['fabric-local']) {
  const loading = ref(false)
  const error = ref('')
  const result = ref<Record<string, unknown> | null>(null)

  async function runSimulate(params: Record<string, unknown> = {}, userPrompt = '') {
    loading.value = true
    error.value = ''
    result.value = null
    try {
      const res = await fetch(`/api/v1/labs/${pluginId}/simulate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_prompt: userPrompt,
          params,
          allowed_chain_ids: defaultChainIds,
        }),
      })
      const data = await res.json()
      if (!res.ok) throw new Error((data as { error?: string }).error || res.statusText)
      result.value = data
    } catch (e) {
      error.value = e instanceof Error ? e.message : String(e)
    } finally {
      loading.value = false
    }
  }

  const evaluation = () => {
    const ev = result.value?.evaluation as Record<string, unknown> | undefined
    return ev ?? null
  }

  return { loading, error, result, runSimulate, evaluation }
}
