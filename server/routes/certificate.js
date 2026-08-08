import { Router } from 'express';
import { body } from 'express-validator';
import { verifyCertificate } from '../controllers/certificateController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/verify', [body('certificateId').notEmpty()], validateRequest, verifyCertificate);

export default router;
