import GalleryItem from '../models/GalleryItem.js';

export const getGallery = async (req, res, next) => {
  try {
    const items = await GalleryItem.find({ status: 'active' }).sort({ createdAt: -1 });
    res.json(items);
  } catch (error) {
    next(error);
  }
};
