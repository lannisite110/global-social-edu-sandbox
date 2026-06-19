/**
 * Static lab component loaders for global-social-edu-sandbox.
 * Imported by core frontend router (vite alias @sandbox).
 */
export const globalSandboxLabs: Record<string, () => Promise<{ default: unknown }>> = {
  'edu.global.sandbox.election': () => import('./election/ElectionLab.vue'),
  'edu.global.sandbox.religion': () => import('./religion/ReligionLab.vue'),
  'edu.global.sandbox.welfare': () => import('./welfare/WelfareLab.vue'),
  'edu.global.sandbox.regulatory': () => import('./regulatory/RegulatoryLab.vue'),
  'edu.global.sandbox.logistics': () => import('./logistics/LogisticsLab.vue'),
}
