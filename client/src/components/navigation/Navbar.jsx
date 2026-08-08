import { useEffect, useState } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { FiMenu, FiX, FiPhone } from 'react-icons/fi';

const links = [
  { label: 'Home', href: '/' },
  { label: 'About', href: '/about' },
  { label: 'Courses', href: '/courses' },
  { label: 'Verify Certificate', href: '/verify-certificate' },
  { label: 'Contact', href: '/contact' }
];

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`sticky top-0 z-40 transition-all duration-300 ${scrolled ? 'backdrop-blur-xl bg-white/90 shadow-sm' : 'bg-transparent'}`}>
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-8">
        <Link to="/" className="flex items-center gap-3 text-lg font-semibold text-slate-900">
          <span className="inline-flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-primary to-secondary text-white shadow-soft">N</span>
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-slate-500">Navankur Ra</p>
            <p className="text-[0.85rem] text-slate-500">Premium Education</p>
          </div>
        </Link>

        <nav className="hidden items-center gap-1 lg:flex">
          {links.map((item) => (
            <NavLink key={item.href} to={item.href} className={({ isActive }) => `rounded-full px-4 py-2 text-sm transition ${isActive ? 'bg-slate-100 text-slate-900' : 'text-slate-600 hover:text-slate-900'}`}>
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="hidden items-center gap-4 lg:flex">
          <Link to="/contact" className="btn-gradient">Get Started</Link>
          <div className="inline-flex items-center gap-2 rounded-full bg-slate-100 px-4 py-2 text-sm text-slate-700">
            <FiPhone />
            <span>+91 98765 43210</span>
          </div>
        </div>

        <button className="inline-flex h-11 w-11 items-center justify-center rounded-full border border-slate-200 bg-white text-slate-700 shadow-sm lg:hidden" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          {open ? <FiX size={20} /> : <FiMenu size={20} />}
        </button>
      </div>

      {open && (
        <div className="border-t border-slate-200 bg-white px-6 py-4 lg:hidden">
          <div className="flex flex-col gap-3">
            {links.map((item) => (
              <NavLink key={item.href} to={item.href} className="rounded-2xl px-4 py-3 text-sm text-slate-700 transition hover:bg-slate-100" onClick={() => setOpen(false)}>
                {item.label}
              </NavLink>
            ))}
            <Link to="/contact" className="btn-gradient" onClick={() => setOpen(false)}>
              Talk to Advisor
            </Link>
          </div>
        </div>
      )}
    </header>
  );
}
