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
  id: 'edu.global.sandbox.welfare',
  title: 'Welfare Anti-Fraud Simulation',
  routePrefix: '/labs/edu.global.sandbox.welfare',
  routes: [{ path: '', component: () => import('./WelfareLab.vue') }],
  apiBase: '/api/v1/labs/edu.global.sandbox.welfare',
}

export default plugin
