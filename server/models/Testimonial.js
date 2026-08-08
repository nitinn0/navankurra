import mongoose from 'mongoose';

const TestimonialSchema = new mongoose.Schema({
  name: { type: String, required: true },
  role: { type: String, required: true },
  review: { type: String, required: true },
  rating: { type: Number, min: 1, max: 5 },
  status: { type: String, enum: ['active', 'hidden'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.Testimonial || mongoose.model('Testimonial', TestimonialSchema);
