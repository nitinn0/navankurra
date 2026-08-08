import mongoose from 'mongoose';

const CourseSchema = new mongoose.Schema({
  title: { type: String, required: true },
  slug: { type: String, required: true, unique: true },
  description: { type: String, required: true },
  duration: { type: String, required: true },
  mode: { type: String, default: 'Online Live' },
  trainer: { type: String, required: true },
  price: { type: Number, required: true },
  status: { type: String, enum: ['active', 'draft'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.Course || mongoose.model('Course', CourseSchema);
