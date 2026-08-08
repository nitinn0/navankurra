import api from './api.js';

export function sendContactMessage(payload) {
  return api.post('/contact', payload);
}
