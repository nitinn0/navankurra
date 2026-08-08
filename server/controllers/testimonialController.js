import Testimonial from '../models/Testimonial.js';

export const getTestimonials = async (req, res, next) => {
  try {
    const items = await Testimonial.find({ status: 'active' }).sort({ createdAt: -1 });
    res.json(items);
  } catch (error) {
    next(error);
  }
};
