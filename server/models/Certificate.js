import mongoose from 'mongoose';

const CertificateSchema = new mongoose.Schema({
  certificateId: { type: String, required: true, unique: true },
  name: { type: String, required: true },
  course: { type: String, required: true },
  issueDate: { type: String, required: true },
  status: { type: String, enum: ['valid', 'revoked'], default: 'valid' }
}, { timestamps: true });

export default mongoose.models.Certificate || mongoose.model('Certificate', CertificateSchema);
