import ContactQuery from '../models/ContactQuery.js';
import { sendEmail } from '../config/mailer.js';

export const submitContact = async (req, res, next) => {
  try {
    const contact = await ContactQuery.create(req.body);
    const html = `
      <h2>New contact inquiry</h2>
      <p><strong>Name:</strong> ${contact.name}</p>
      <p><strong>Phone:</strong> ${contact.phone}</p>
      <p><strong>Email:</strong> ${contact.email}</p>
      <p><strong>Subject:</strong> ${contact.subject}</p>
      <p><strong>Message:</strong> ${contact.message}</p>
    `;
    await sendEmail({ to: process.env.EMAIL_FROM, subject: 'New contact inquiry', html });
    res.status(201).json({ message: 'Contact inquiry saved successfully' });
  } catch (error) {
    next(error);
  }
};
