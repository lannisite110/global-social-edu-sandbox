export interface LabPlugin {
  id: string
  title: string
  routePrefix: string
  routes: Array<{
    path: string
    component: () => Promise<unknown>
  }>
  apiBase: string
}

export const plugin: LabPlugin = {
  id: 'edu.global.sandbox.election',
  title: 'Election Hash Consensus Demo',
  routePrefix: '/labs/edu.global.sandbox.election',
  routes: [{ path: '', component: () => import('./ElectionLab.vue') }],
  apiBase: '/api/v1/labs/edu.global.sandbox.election',
}

export default plugin
