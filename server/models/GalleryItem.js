import mongoose from 'mongoose';

const GalleryItemSchema = new mongoose.Schema({
  title: { type: String, required: true },
  imageUrl: { type: String, required: true },
  status: { type: String, enum: ['active', 'hidden'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.GalleryItem || mongoose.model('GalleryItem', GalleryItemSchema);
