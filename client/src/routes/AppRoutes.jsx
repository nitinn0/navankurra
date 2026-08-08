import { Route, Routes } from 'react-router-dom';
import About from '../pages/About.jsx';
import AdminDashboard from '../pages/AdminDashboard.jsx';
import AdminLogin from '../pages/AdminLogin.jsx';
import CourseDetails from '../pages/CourseDetails.jsx';
import Courses from '../pages/Courses.jsx';
import Contact from '../pages/Contact.jsx';
import Home from '../pages/Home.jsx';
import NotFound from '../pages/NotFound.jsx';
import PrivacyPolicy from '../pages/PrivacyPolicy.jsx';
import TermsConditions from '../pages/TermsConditions.jsx';
import VerifyCertificate from '../pages/VerifyCertificate.jsx';

export default function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/courses" element={<Courses />} />
      <Route path="/course/:slug" element={<CourseDetails />} />
      <Route path="/verify-certificate" element={<VerifyCertificate />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/privacy-policy" element={<PrivacyPolicy />} />
      <Route path="/terms-conditions" element={<TermsConditions />} />
      <Route path="/admin" element={<AdminDashboard />} />
      <Route path="/admin/login" element={<AdminLogin />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}
