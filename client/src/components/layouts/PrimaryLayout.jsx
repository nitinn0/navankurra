import Navbar from '../navigation/Navbar.jsx';
import Footer from '../navigation/Footer.jsx';
import ScrollToTop from '../ui/ScrollToTop.jsx';

export default function PrimaryLayout({ children }) {
  return (
    <div className="min-h-screen overflow-hidden bg-slate-50 text-slate-900">
      <Navbar />
      <main>{children}</main>
      <Footer />
      <ScrollToTop />
    </div>
  );
}
