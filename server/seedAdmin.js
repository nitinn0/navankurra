import dotenv from 'dotenv';
dotenv.config();

import mongoose from 'mongoose';
import User from './models/User.js';

const run = async () => {
  try {
    if (!process.env.MONGO_URI) {
      throw new Error('MONGO_URI is not defined in server/.env');
    }

    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });

    const email = 'info@navankurra.com';
    const password = 'Navankurra@12';

    const admin = await User.findOneAndUpdate(
      { email },
      {
        name: 'Navankur Ra Admin',
        email,
        password,
        role: 'admin',
        status: 'active'
      },
      {
        new: true,
        upsert: true,
        setDefaultsOnInsert: true,
        runValidators: true
      }
    );

    console.log('Admin user created/updated:', {
      id: admin._id,
      name: admin.name,
      email: admin.email,
      role: admin.role,
      status: admin.status
    });
  } catch (error) {
    console.error('Admin seed failed:', error.message);
  } finally {
    await mongoose.disconnect();
  }
};

run();
