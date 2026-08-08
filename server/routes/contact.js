import { Router } from 'express';
import { body } from 'express-validator';
import { submitContact } from '../controllers/contactController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/', [
  body('name').notEmpty(),
  body('phone').notEmpty(),
  body('email').isEmail(),
  body('subject').notEmpty(),
  body('message').notEmpty()
], validateRequest, submitContact);

export default router;
