import { Router } from 'express';
import { adminDashboard, adminCourses } from '../controllers/adminController.js';
import { authenticate, requireAdmin } from '../middleware/auth.js';

const router = Router();

router.use(authenticate, requireAdmin);
router.get('/dashboard', adminDashboard);
router.get('/courses', adminCourses);

export default router;
