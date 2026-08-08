import { Link } from 'react-router-dom';
import { FiMail, FiMapPin, FiPhone, FiChevronRight } from 'react-icons/fi';

const quickLinks = [
  { label: 'Home', href: '/' },
  { label: 'About', href: '/about' },
  { label: 'Courses', href: '/courses' },
  { label: 'Contact', href: '/contact' }
];

export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-white py-16">
      <div className="mx-auto grid max-w-7xl gap-10 px-6 lg:grid-cols-4 lg:px-8">
        <div className="space-y-4">
          <div className="inline-flex h-12 w-12 items-center justify-center rounded-3xl bg-gradient-to-br from-primary to-secondary text-white shadow-soft">N</div>
          <p className="max-w-sm text-sm leading-7 text-slate-600">
            Navankur Ra is a modern education brand focused on live training, certification, and career-focused course delivery.
          </p>
          <div className="space-y-2 text-sm text-slate-600">
            <p className="inline-flex items-center gap-2"><FiMapPin /> Mumbai, India</p>
            <p className="inline-flex items-center gap-2"><FiPhone /> +91 98765 43210</p>
            <p className="inline-flex items-center gap-2"><FiMail /> info@navankurra.com</p>
          </div>
        </div>

        <div>
          <h3 className="mb-5 text-sm font-semibold uppercase tracking-[0.24em] text-slate-900">Quick Links</h3>
          <div className="space-y-3 text-sm text-slate-600">
            {quickLinks.map((link) => (
              <Link key={link.href} to={link.href} className="flex items-center gap-2 transition hover:text-slate-900">
                <FiChevronRight /> {link.label}
              </Link>
            ))}
          </div>
        </div>

        <div>
          <h3 className="mb-5 text-sm font-semibold uppercase tracking-[0.24em] text-slate-900">Courses</h3>
          <div className="space-y-3 text-sm text-slate-600">
            <p>Full Stack Development</p>
            <p>Data Science</p>
            <p>Cloud Engineering</p>
            <p>Digital Marketing</p>
          </div>
        </div>

        <div>
          <h3 className="mb-5 text-sm font-semibold uppercase tracking-[0.24em] text-slate-900">Stay Updated</h3>
          <p className="mb-5 max-w-sm text-sm leading-7 text-slate-600">Subscribe for launch updates, course openings, and scholarship alerts.</p>
          <div className="flex gap-2">
            <input type="email" placeholder="Enter your email" className="w-full rounded-3xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-700 outline-none transition focus:border-primary" />
            <button className="btn-gradient">Subscribe</button>
          </div>
        </div>
      </div>
      <div className="mt-10 border-t border-slate-200 pt-6 text-center text-sm text-slate-500">© 2026 Navankur Ra. All rights reserved.</div>
    </footer>
  );
}
