import api from './api.js';

export function verifyCertificate(payload) {
  return api.post('/certificate/verify', payload);
}
