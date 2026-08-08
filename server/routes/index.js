import { Router } from 'express';
import courseRoutes from './courses.js';
import contactRoutes from './contact.js';
import certificateRoutes from './certificate.js';
import authRoutes from './auth.js';
import testimonialRoutes from './testimonials.js';
import galleryRoutes from './gallery.js';
import adminRoutes from './admin.js';

const router = Router();
router.use('/admin', adminRoutes);
router.use('/courses', courseRoutes);
router.use('/contact', contactRoutes);
router.use('/certificate', certificateRoutes);
router.use('/auth', authRoutes);
router.use('/testimonials', testimonialRoutes);
router.use('/gallery', galleryRoutes);

router.get('/', (req, res) => res.json({ status: 'ok', message: 'Navankur Ra API is running' }));

export default router;
