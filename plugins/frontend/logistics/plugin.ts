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
  id: 'edu.global.sandbox.logistics',
  title: 'Logistics Audit Ledger Demo',
  routePrefix: '/labs/edu.global.sandbox.logistics',
  routes: [{ path: '', component: () => import('./LogisticsLab.vue') }],
  apiBase: '/api/v1/labs/edu.global.sandbox.logistics',
}

export default plugin
