import api from './api.js';

export function fetchCourses() {
  return api.get('/courses');
}

export function fetchCourseBySlug(slug) {
  return api.get(`/courses/${slug}`);
}
