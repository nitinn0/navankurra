import { Router } from 'express';
import { body } from 'express-validator';
import { login } from '../controllers/authController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/login', [body('email').isEmail(), body('password').notEmpty()], validateRequest, login);
export default router;
