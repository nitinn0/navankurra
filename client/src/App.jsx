import { AnimatePresence, motion } from 'framer-motion';
import { useLocation } from 'react-router-dom';
import AppRoutes from './routes/AppRoutes.jsx';
import PrimaryLayout from './components/layouts/PrimaryLayout.jsx';

export default function App() {
  const location = useLocation();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={location.pathname}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.35 }}
      >
        <PrimaryLayout>
          <AppRoutes />
        </PrimaryLayout>
      </motion.div>
    </AnimatePresence>
  );
}
