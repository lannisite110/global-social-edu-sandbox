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
  id: 'edu.global.sandbox.religion',
  title: 'Religion Rule Sandbox',
  routePrefix: '/labs/edu.global.sandbox.religion',
  routes: [{ path: '', component: () => import('./ReligionLab.vue') }],
  apiBase: '/api/v1/labs/edu.global.sandbox.religion',
}

export default plugin
