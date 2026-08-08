import Certificate from '../models/Certificate.js';

export const verifyCertificate = async (req, res, next) => {
  try {
    const certificate = await Certificate.findOne({ certificateId: req.body.certificateId });
    if (!certificate) return res.status(404).json({ message: 'Certificate not found' });
    res.json(certificate);
  } catch (error) {
    next(error);
  }
};
