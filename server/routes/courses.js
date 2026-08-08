import { Router } from 'express';
import { body } from 'express-validator';
import { getCourses, getCourseBySlug, createCourse, updateCourse, deleteCourse } from '../controllers/courseController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.get('/', getCourses);
router.get('/:slug', getCourseBySlug);
router.post('/', [body('title').notEmpty(), body('slug').notEmpty(), body('description').notEmpty()], validateRequest, createCourse);
router.put('/:id', [body('title').optional().notEmpty(), body('description').optional().notEmpty()], validateRequest, updateCourse);
router.delete('/:id', deleteCourse);

export default router;
