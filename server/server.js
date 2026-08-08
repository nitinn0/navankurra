import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import helmet from 'helmet';
import connectDB from './config/db.js';
import routes from './routes/index.js';
import rateLimiter from './middleware/rateLimiter.js';
import errorHandler from './middleware/errorHandler.js';

dotenv.config();
const app = express();
const port = process.env.PORT || 5000;

connectDB();
app.use(helmet());
app.use(cors({ origin: ['http://localhost:5173'], credentials: true }));
app.use(express.json());
app.use(rateLimiter);
app.use('/api', routes);
app.use(errorHandler);

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
