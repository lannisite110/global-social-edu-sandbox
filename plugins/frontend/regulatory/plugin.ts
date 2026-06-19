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
  id: 'edu.global.sandbox.regulatory',
  title: 'Regulatory Rule Sandbox',
  routePrefix: '/labs/edu.global.sandbox.regulatory',
  routes: [{ path: '', component: () => import('./RegulatoryLab.vue') }],
  apiBase: '/api/v1/labs/edu.global.sandbox.regulatory',
}

export default plugin
