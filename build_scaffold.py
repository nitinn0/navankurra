from pathlib import Path

files = {
    'README.md': '''# Navankurra Education Platform

Modern MERN starter project for a premium educational website.

## Structure

- `client/` - Vite React frontend with Tailwind, Framer Motion, and SEO-ready layout.
- `server/` - Express API with MongoDB, authentication, contact/email integration, and admin-ready routes.

## Getting Started

1. Install dependencies
   - `cd client && npm install`
   - `cd ../server && npm install`
2. Copy `.env.example` to `.env` in the `server` folder and configure it.
3. Run the development servers:
   - `cd client && npm run dev`
   - `cd ../server && npm run dev`
''',
    '.gitignore': '''node_modules
.DS_Store
/client/dist
/server/node_modules
/server/.env
''',
    'client/package.json': '''{
  "name": "navankur-ra-client",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext .js,.jsx",
    "format": "prettier --write ."
  },
  "dependencies": {
    "axios": "^1.6.4",
    "framer-motion": "^11.3.5",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-hook-form": "^7.57.0",
    "react-hot-toast": "^2.4.1",
    "react-icons": "^4.11.0",
    "react-router-dom": "^6.18.1",
    "swiper": "^10.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.3.3",
    "autoprefixer": "^10.4.19",
    "eslint": "^8.57.0",
    "eslint-config-prettier": "^9.0.0",
    "eslint-plugin-react": "^7.34.1",
    "eslint-plugin-react-hooks": "^4.6.0",
    "postcss": "^8.4.35",
    "prettier": "^3.6.0",
    "tailwindcss": "^3.4.4",
    "vite": "^5.4.1"
  }
}
''',
    'client/vite.config.js': '''import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()]
});
''',
    'client/tailwind.config.js': '''export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#4f46e5',
          light: '#818cf8',
          dark: '#3730a3'
        },
        secondary: {
          DEFAULT: '#ec4899',
          light: '#f472b6',
          dark: '#be185d'
        }
      },
      boxShadow: {
        soft: '0 20px 60px rgba(15, 23, 42, 0.08)'
      },
      backgroundImage: {
        'hero-gradient': "radial-gradient(circle at top right, rgba(79, 70, 229, 0.2), transparent 36%), radial-gradient(circle at bottom left, rgba(236, 72, 153, 0.16), transparent 28%)"
      }
    }
  },
  plugins: []
};
''',
    'client/postcss.config.js': '''export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {}
  }
};
''',
    'client/jsconfig.json': '''{
  "compilerOptions": {
    "baseUrl": "./src",
    "paths": {
      "@/*": ["*"]
    }
  }
}
''',
    'client/index.html': '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Navankurra | Modern EdTech Platform</title>
    <meta name="description" content="Navankurra offers premium live courses, certificates, and career support for learners who want to accelerate their skill journey." />
    <meta property="og:title" content="Navankurra | Premium EdTech Courses" />
    <meta property="og:description" content="Modern education platform with live training, certifications, and placement support." />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  </head>
  <body class="bg-slate-50 text-slate-900">
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
''',
    'client/src/main.jsx': '''import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
      <Toaster position="top-right" />
    </BrowserRouter>
  </React.StrictMode>
);
''',
    'client/src/App.jsx': '''import { AnimatePresence, motion } from 'framer-motion';
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
''',
    'client/src/index.css': '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  color-scheme: light;
}

html {
  scroll-behavior: smooth;
}

body {
  min-height: 100vh;
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 100%);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

#root {
  isolation: isolate;
}

::selection {
  background: rgba(79, 70, 229, 0.14);
  color: #111827;
}

.btn-gradient {
  @apply inline-flex items-center justify-center rounded-full bg-gradient-to-r from-primary to-secondary px-6 py-3 text-sm font-semibold text-white shadow-soft transition duration-300 ease-out hover:scale-[1.01];
}

.card-glass {
  @apply rounded-3xl border border-white/60 bg-white/80 shadow-soft backdrop-blur-xl;
}
''',
    'client/src/routes/AppRoutes.jsx': '''import { Route, Routes } from 'react-router-dom';
import About from '../pages/About.jsx';
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
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}
''',
    'client/src/components/layouts/PrimaryLayout.jsx': '''import Navbar from '../navigation/Navbar.jsx';
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
''',
    'client/src/components/navigation/Navbar.jsx': '''import { useEffect, useState } from 'react';
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
            <p className="text-sm font-semibold uppercase tracking-[0.24em] text-slate-500">Navankurra</p>
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
''',
    'client/src/components/navigation/Footer.jsx': '''import { Link } from 'react-router-dom';
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
            Navankurra is a modern education brand focused on live training, certification, and career-focused course delivery.
          </p>
          <div className="space-y-2 text-sm text-slate-600">
            <p className="inline-flex items-center gap-2"><FiMapPin />  </p>
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
      <div className="mt-10 border-t border-slate-200 pt-6 text-center text-sm text-slate-500">© 2026 Navankurra. All rights reserved.</div>
    </footer>
  );
}
''',
    'client/src/components/ui/ScrollToTop.jsx': '''import { useEffect, useState } from 'react';
import { FiChevronUp } from 'react-icons/fi';

export default function ScrollToTop() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const handler = () => setVisible(window.scrollY > 400);
    window.addEventListener('scroll', handler);
    return () => window.removeEventListener('scroll', handler);
  }, []);

  return (
    <button
      type="button"
      onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
      className={`fixed bottom-6 right-6 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full bg-primary text-white shadow-soft transition-opacity ${visible ? 'opacity-100' : 'pointer-events-none opacity-0'}`}
      aria-label="Scroll to top"
    >
      <FiChevronUp size={20} />
    </button>
  );
}
''',
    'client/src/components/ui/SectionTitle.jsx': '''export default function SectionTitle({ eyebrow, title, description }) {
  return (
    <div className="max-w-2xl space-y-3">
      {eyebrow && <p className="text-sm font-semibold uppercase tracking-[0.28em] text-secondary">{eyebrow}</p>}
      <h2 className="text-3xl font-semibold text-slate-900 sm:text-4xl">{title}</h2>
      {description && <p className="text-slate-600">{description}</p>}
    </div>
  );
}
''',
    'client/src/components/courses/CourseCard.jsx': '''import { Link } from 'react-router-dom';
import { FiClock, FiMonitor, FiUsers } from 'react-icons/fi';

export default function CourseCard({ course }) {
  return (
    <article className="card-glass overflow-hidden rounded-[32px] border border-white/60 p-6 shadow-soft transition duration-300 hover:-translate-y-1 hover:border-primary/20">
      <div className="mb-5 h-52 rounded-3xl bg-slate-200"></div>
      <div className="space-y-4">
        <div className="flex flex-wrap items-center gap-3 text-xs uppercase tracking-[0.24em] text-slate-500">
          <span>{course.mode}</span>
          <span>•</span>
          <span>{course.duration}</span>
        </div>
        <h3 className="text-xl font-semibold text-slate-900">{course.title}</h3>
        <p className="text-sm leading-7 text-slate-600">{course.description}</p>
        <div className="grid gap-3 text-sm text-slate-600 sm:grid-cols-3">
          <span className="inline-flex items-center gap-2"><FiMonitor /> {course.type}</span>
          <span className="inline-flex items-center gap-2"><FiClock /> {course.duration}</span>
          <span className="inline-flex items-center gap-2"><FiUsers /> {course.trainer}</span>
        </div>
      </div>
      <div className="mt-6 flex items-center justify-between gap-4">
        <p className="text-xl font-semibold text-slate-900">₹{course.price}</p>
        <Link to={`/course/${course.slug}`} className="rounded-full bg-primary px-5 py-3 text-sm font-semibold text-white transition hover:bg-primary/90">
          View Details
        </Link>
      </div>
    </article>
  );
}
''',
    'client/src/data/courses.js': '''export const courses = [
  {
    id: 'course-fullstack-1',
    slug: 'full-stack-web-development',
    title: 'Full Stack Web Development',
    description: 'Build modern applications using React, Node.js, Express, and MongoDB.',
    duration: '6 Months',
    mode: 'Online Live',
    type: 'Live sessions',
    trainer: 'Rahul Sharma',
    price: 39999,
    level: 'Beginner'
  },
  {
    id: 'course-data-1',
    slug: 'data-science-bootcamp',
    title: 'Data Science Bootcamp',
    description: 'Master data pipelines, machine learning, and visualization for business insight.',
    duration: '5 Months',
    mode: 'Online Live',
    type: 'Live sessions',
    trainer: 'Pooja Singh',
    price: 34999,
    level: 'Intermediate'
  },
  {
    id: 'course-cloud-1',
    slug: 'cloud-engineering-pro',
    title: 'Cloud Engineering Pro',
    description: 'Deploy scalable apps with AWS, Docker, Kubernetes, and CI/CD workflows.',
    duration: '4 Months',
    mode: 'Online Live',
    type: 'Project-based',
    trainer: 'Amit Gupta',
    price: 29999,
    level: 'Intermediate'
  }
];
''',
    'client/src/data/testimonials.js': '''export const testimonials = [
  {
    id: 'testimonial-1',
    name: 'Aarav Patel',
    rating: 5,
    review: 'The mentorship and live projects helped me land a Developer role in under 4 months.',
    role: 'Full Stack Developer'
  },
  {
    id: 'testimonial-2',
    name: 'Nisha Reddy',
    rating: 5,
    review: 'The curriculum is modern, relevant, and delivered with excellent support throughout.',
    role: 'Data Analyst'
  },
  {
    id: 'testimonial-3',
    name: 'Vikram Singh',
    rating: 5,
    review: 'I enjoyed the industry-backed projects and the placement guidance from the team.',
    role: 'Cloud Engineer'
  }
];
''',
    'client/src/services/api.js': '''import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api',
  timeout: 10000
});

export default api;
''',
    'client/src/services/courseService.js': '''import api from './api.js';

export function fetchCourses() {
  return api.get('/courses');
}

export function fetchCourseBySlug(slug) {
  return api.get(`/courses/${slug}`);
}
''',
    'client/src/services/contactService.js': '''import api from './api.js';

export function sendContactMessage(payload) {
  return api.post('/contact', payload);
}
''',
    'client/src/services/certificateService.js': '''import api from './api.js';

export function verifyCertificate(payload) {
  return api.post('/certificate/verify', payload);
}
''',
    'client/src/hooks/useDebounce.js': '''import { useEffect, useState } from 'react';

export default function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timeout = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timeout);
  }, [value, delay]);

  return debounced;
}
''',
    'client/src/utils/SEO.jsx': '''import { Helmet } from 'react-helmet';

export default function SEO({ title, description, url }) {
  return (
    <Helmet>
      <title>{title}</title>
      <meta name="description" content={description} />
      <meta property="og:title" content={title} />
      <meta property="og:description" content={description} />
      <meta property="og:url" content={url || window.location.href} />
      <meta property="og:type" content="website" />
      <meta name="twitter:card" content="summary_large_image" />
    </Helmet>
  );
}
''',
    'client/src/pages/Home.jsx': '''import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import SectionTitle from '../components/ui/SectionTitle.jsx';
import CourseCard from '../components/courses/CourseCard.jsx';
import { courses } from '../data/courses.js';
import { testimonials } from '../data/testimonials.js';

const stats = [
  { label: 'Students trained', value: '12K+' },
  { label: 'Live courses', value: '24+' },
  { label: 'Placement support', value: '98%' },
  { label: 'Certificates issued', value: '10K+' }
];

export default function Home() {
  return (
    <section className="relative overflow-hidden pb-20 pt-24">
      <div className="absolute inset-x-0 top-0 h-[420px] bg-hero-gradient opacity-90" />
      <div className="relative mx-auto max-w-7xl px-6 lg:px-8">
        <div className="grid gap-14 lg:grid-cols-[1.15fr_0.85fr] lg:items-center">
          <motion.div initial={{ opacity: 0, y: 30 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }} className="space-y-8 py-16 lg:py-24">
            <span className="inline-flex rounded-full bg-white/80 px-4 py-2 text-xs font-semibold uppercase tracking-[0.35em] text-secondary shadow-soft backdrop-blur-xl">Premium learning for modern professionals</span>
            <h1 className="max-w-3xl text-5xl font-semibold tracking-tight text-slate-950 sm:text-6xl">Upskill with career-focused courses crafted for the next generation.</h1>
            <p className="max-w-2xl text-lg leading-8 text-slate-600">Join live classes, build real projects, earn verified certificates, and access personalized placement support from industry experts.</p>
            <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
              <Link to="/courses" className="btn-gradient">Explore courses</Link>
              <Link to="/contact" className="inline-flex items-center justify-center rounded-full border border-slate-200 bg-white px-6 py-3 text-sm font-semibold text-slate-900 transition hover:border-primary/70 hover:text-slate-900">
                Talk with admissions
              </Link>
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              {stats.map((item) => (
                <div key={item.label} className="rounded-3xl bg-white/90 p-5 shadow-soft backdrop-blur-xl">
                  <p className="text-3xl font-semibold text-slate-900">{item.value}</p>
                  <p className="mt-2 text-sm uppercase tracking-[0.24em] text-slate-500">{item.label}</p>
                </div>
              ))}
            </div>
          </motion.div>

          <motion.div initial={{ opacity: 0, x: 40 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.7 }} className="relative rounded-[40px] bg-white/90 p-8 shadow-soft backdrop-blur-xl ring-1 ring-slate-200 lg:p-10">
            <div className="absolute inset-x-0 top-0 h-40 rounded-b-[40px] bg-gradient-to-br from-primary/20 to-secondary/10" />
            <div className="relative space-y-6 pt-10">
              <div className="rounded-[28px] border border-slate-200 bg-slate-50 p-6">
                <p className="text-sm uppercase tracking-[0.3em] text-secondary">Why choose us</p>
                <ul className="mt-4 space-y-4 text-sm leading-7 text-slate-600">
                  <li>Industry-aligned curriculum</li>
                  <li>Live mentorship and project guidance</li>
                  <li>Certification and placement coaching</li>
                </ul>
              </div>
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-white p-5 shadow-sm">
                  <h3 className="font-semibold text-slate-900">Experienced trainers</h3>
                  <p className="mt-3 text-sm text-slate-600">Mentors with real production and hiring experience.</p>
                </div>
                <div className="rounded-3xl bg-white p-5 shadow-sm">
                  <h3 className="font-semibold text-slate-900">Live projects</h3>
                  <p className="mt-3 text-sm text-slate-600">Build portfolio-ready work while learning.</p>
                </div>
                <div className="rounded-3xl bg-white p-5 shadow-sm">
                  <h3 className="font-semibold text-slate-900">Certification</h3>
                  <p className="mt-3 text-sm text-slate-600">Verified credentials for shared portfolios.</p>
                </div>
                <div className="rounded-3xl bg-white p-5 shadow-sm">
                  <h3 className="font-semibold text-slate-900">Career support</h3>
                  <p className="mt-3 text-sm text-slate-600">Assistance with interviews, resumes, and placements.</p>
                </div>
              </div>
            </div>
          </motion.div>
        </div>

        <div className="space-y-20">
          <section className="space-y-8 pt-8">
            <SectionTitle eyebrow="Popular courses" title="Learn with the best programs" description="Select the course that fits your goals and start building skills that employers value." />
            <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
              {courses.map((course) => (
                <CourseCard key={course.id} course={course} />
              ))}
            </div>
          </section>

          <section className="space-y-8">
            <SectionTitle eyebrow="Learning journey" title="A streamlined path to success" description="From course selection to career support, every step is planned for high-impact learning." />
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
              {['Choose Course', 'Enroll', 'Learn', 'Certification', 'Career Support'].map((step, index) => (
                <div key={step} className="rounded-3xl border border-slate-200 bg-white p-6 text-center shadow-sm">
                  <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-primary text-white">{index + 1}</div>
                  <p className="font-semibold text-slate-900">{step}</p>
                </div>
              ))}
            </div>
          </section>

          <section className="space-y-8">
            <SectionTitle eyebrow="Testimonials" title="Students love the experience" description="Real reviews from learners who improved their careers and confidence." />
            <div className="grid gap-6 md:grid-cols-3">
              {testimonials.map((item) => (
                <motion.div key={item.id} whileHover={{ y: -5 }} className="card-glass rounded-[32px] p-8 shadow-soft">
                  <p className="mb-6 text-slate-600">“{item.review}”</p>
                  <div className="space-y-2">
                    <p className="font-semibold text-slate-900">{item.name}</p>
                    <p className="text-sm text-slate-500">{item.role}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </section>

          <section className="rounded-[40px] bg-slate-950/95 p-10 text-white shadow-soft">
            <div className="grid gap-8 lg:grid-cols-[1fr_0.8fr] lg:items-center">
              <div className="space-y-4">
                <p className="text-sm uppercase tracking-[0.35em] text-secondary">Ready to learn</p>
                <h2 className="text-3xl font-semibold sm:text-4xl">Start your career transformation today.</h2>
                <p className="max-w-xl text-slate-300">Speak with our advisors and get a personalised learning plan for your next role.</p>
              </div>
              <Link to="/contact" className="inline-flex items-center justify-center rounded-full bg-white px-8 py-4 text-sm font-semibold text-slate-950 transition hover:bg-slate-100">
                Contact admissions
              </Link>
            </div>
          </section>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/About.jsx': '''import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function About() {
  return (
    <section className="bg-slate-50 py-24">
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="rounded-[40px] bg-white p-10 shadow-soft">
          <SectionTitle eyebrow="About Us" title="We help learners build modern careers through immersive education." description="Navankurra brings curated live programs, expert mentoring, and real-world certification to ambitious learners." />

          <div className="mt-16 grid gap-8 lg:grid-cols-[0.95fr_0.85fr] lg:items-start">
            <div className="space-y-8">
              <div className="space-y-4 rounded-3xl border border-slate-200 bg-slate-50 p-7">
                <h3 className="text-xl font-semibold text-slate-900">Our story</h3>
                <p className="text-slate-600 leading-8">Founded to make premium technical training accessible, we blend practical coursework with mentorship, guided practice, and placement support.</p>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-white p-7 shadow-sm">
                  <h4 className="font-semibold text-slate-900">Mission</h4>
                  <p className="mt-3 text-slate-600">Empower learners with relevant skills, real projects, and a direct path to career growth.</p>
                </div>
                <div className="rounded-3xl bg-white p-7 shadow-sm">
                  <h4 className="font-semibold text-slate-900">Vision</h4>
                  <p className="mt-3 text-slate-600">Create a trusted education brand known for outcomes, innovation, and learner-first experiences.</p>
                </div>
              </div>
            </div>

            <div className="space-y-8">
              <div className="rounded-[32px] bg-gradient-to-br from-primary to-secondary p-8 text-white shadow-soft">
                <p className="text-sm uppercase tracking-[0.3em] text-white/80">Founder message</p>
                <h3 className="mt-5 text-3xl font-semibold">“Every learner deserves a modern education journey that leads to real results.”</h3>
                <p className="mt-4 text-slate-100 leading-8">We combine faculty expertise, live interaction, and career coaching to make the next step clear and achievable.</p>
              </div>
              <div className="grid gap-4 sm:grid-cols-2">
                {['Value-driven curriculum', 'Industry mentors', 'Project-based training', 'Career support'].map((item) => (
                  <div key={item} className="rounded-3xl bg-slate-50 p-6 shadow-sm">
                    <p className="font-semibold text-slate-900">{item}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/Courses.jsx': '''import { useEffect, useMemo, useState } from 'react';
import { FiSearch } from 'react-icons/fi';
import CourseCard from '../components/courses/CourseCard.jsx';
import SectionTitle from '../components/ui/SectionTitle.jsx';
import useDebounce from '../hooks/useDebounce.js';
import { courses as courseData } from '../data/courses.js';

const categories = ['All', 'Web Development', 'Data Science', 'Cloud'];
const durations = ['All', '3 Months', '4 Months', '5 Months', '6 Months'];
const modeOptions = ['All', 'Online Live', 'Offline'];
const priceOptions = ['All', 'Under 30K', '30K-40K', 'Above 40K'];

export default function Courses() {
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('All');
  const [duration, setDuration] = useState('All');
  const [mode, setMode] = useState('All');
  const [price, setPrice] = useState('All');
  const [sort, setSort] = useState('Newest');
  const [page, setPage] = useState(1);
  const debouncedSearch = useDebounce(search, 350);

  const filteredCourses = useMemo(() => {
    return courseData
      .filter((course) => course.title.toLowerCase().includes(debouncedSearch.toLowerCase()))
      .filter((course) => (category === 'All' ? true : course.title.includes(category) || course.type.includes(category)))
      .filter((course) => (duration === 'All' ? true : course.duration === duration))
      .filter((course) => (mode === 'All' ? true : course.mode === mode))
      .filter((course) => {
        if (price === 'All') return true;
        if (price === 'Under 30K') return course.price < 30000;
        if (price === '30K-40K') return course.price >= 30000 && course.price <= 40000;
        return course.price > 40000;
      })
      .sort((a, b) => {
        if (sort === 'Lowest price') return a.price - b.price;
        if (sort === 'Highest price') return b.price - a.price;
        return a.title.localeCompare(b.title);
      });
  }, [category, debouncedSearch, duration, mode, price, sort]);

  const totalPages = Math.max(1, Math.ceil(filteredCourses.length / 6));
  const visibleCourses = filteredCourses.slice((page - 1) * 6, page * 6);

  useEffect(() => {
    setPage(1);
  }, [debouncedSearch, category, duration, mode, price, sort]);

  return (
    <section className="py-20">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <SectionTitle eyebrow="Courses" title="Find the right program for your goals" description="Filter by category, duration, pricing, and delivery model to discover the best fit." />

        <div className="mt-12 grid gap-8 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="space-y-8">
            <div className="rounded-[32px] bg-white p-6 shadow-soft">
              <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
                <div className="relative flex-1">
                  <FiSearch className="pointer-events-none absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-slate-400" />
                  <input
                    type="search"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                    placeholder="Search course title or keyword"
                    className="w-full rounded-3xl border border-slate-200 bg-slate-50 px-12 py-4 text-sm text-slate-800 outline-none transition focus:border-primary"
                  />
                </div>
                <select className="rounded-3xl border border-slate-200 bg-white px-4 py-4 text-sm text-slate-700 outline-none" value={sort} onChange={(e) => setSort(e.target.value)}>
                  <option>Newest</option>
                  <option>Lowest price</option>
                  <option>Highest price</option>
                </select>
              </div>

              <div className="mt-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={category} onChange={(e) => setCategory(e.target.value)}>
                  {categories.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={duration} onChange={(e) => setDuration(e.target.value)}>
                  {durations.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={mode} onChange={(e) => setMode(e.target.value)}>
                  {modeOptions.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
                <select className="rounded-3xl border border-slate-200 bg-slate-50 px-4 py-4 text-sm text-slate-700 outline-none" value={price} onChange={(e) => setPrice(e.target.value)}>
                  {priceOptions.map((item) => (
                    <option key={item}>{item}</option>
                  ))}
                </select>
              </div>
            </div>

            <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
              {visibleCourses.map((course) => (
                <CourseCard key={course.id} course={course} />
              ))}
            </div>

            <div className="flex flex-wrap items-center justify-between gap-3 rounded-3xl bg-white p-6 shadow-soft">
              <p className="text-sm text-slate-600">Showing {visibleCourses.length} of {filteredCourses.length} courses</p>
              <div className="flex flex-wrap items-center gap-2">
                {Array.from({ length: totalPages }, (_, index) => (
                  <button
                    key={index + 1}
                    className={`rounded-full px-4 py-2 text-sm font-semibold transition ${page === index + 1 ? 'bg-primary text-white' : 'bg-slate-100 text-slate-700 hover:bg-slate-200'}`}
                    onClick={() => setPage(index + 1)}
                  >
                    {index + 1}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <aside className="space-y-6 rounded-[32px] bg-white p-6 shadow-soft">
            <div className="rounded-[28px] bg-primary px-6 py-8 text-white shadow-lg">
              <p className="text-sm uppercase tracking-[0.28em] text-white/80">Need guidance?</p>
              <h3 className="mt-4 text-2xl font-semibold">Book a free consultation</h3>
              <p className="mt-4 text-sm leading-7 text-white/90">Talk to our admissions team and choose the option that fits you.</p>
              <a href="/contact" className="mt-6 inline-flex rounded-full bg-white px-5 py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-100">Contact us</a>
            </div>
            <div className="space-y-4 rounded-[28px] border border-slate-200 bg-slate-50 p-6">
              <p className="text-sm uppercase tracking-[0.3em] text-slate-500">Why learners choose us</p>
              <ul className="space-y-3 text-slate-600">
                <li>Expert-led training</li>
                <li>Live project portfolio</li>
                <li>One-on-one review</li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/CourseDetails.jsx': '''import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { courses } from '../data/courses.js';
import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function CourseDetails() {
  const { slug } = useParams();
  const [course, setCourse] = useState(null);

  useEffect(() => {
    const found = courses.find((item) => item.slug === slug);
    setCourse(found ?? null);
  }, [slug]);

  if (!course) {
    return (
      <section className="py-24">
        <div className="mx-auto max-w-5xl px-6 text-center">
          <h2 className="text-3xl font-semibold text-slate-900">Course not found</h2>
          <p className="mt-4 text-slate-600">Please go back to the course catalog and choose another program.</p>
        </div>
      </section>
    );
  }

  return (
    <section className="py-20">
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="space-y-8 rounded-[40px] bg-white p-10 shadow-soft">
          <div className="grid gap-10 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
            <div className="space-y-6">
              <p className="text-sm uppercase tracking-[0.3em] text-secondary">Course details</p>
              <h1 className="text-4xl font-semibold text-slate-950">{course.title}</h1>
              <p className="max-w-2xl text-lg leading-8 text-slate-600">{course.description}</p>
              <div className="grid gap-4 sm:grid-cols-3">
                <div className="rounded-3xl bg-slate-50 p-5 text-sm text-slate-700">Duration: {course.duration}</div>
                <div className="rounded-3xl bg-slate-50 p-5 text-sm text-slate-700">Mode: {course.mode}</div>
                <div className="rounded-3xl bg-slate-50 p-5 text-sm text-slate-700">Price: ₹{course.price}</div>
              </div>
            </div>
            <div className="rounded-[32px] bg-gradient-to-br from-primary to-secondary p-8 text-white shadow-soft">
              <p className="text-sm uppercase tracking-[0.3em] text-white/80">Quick Apply</p>
              <h2 className="mt-4 text-3xl font-semibold">Secure your seat now</h2>
              <p className="mt-4 text-slate-100 leading-7">Enroll in the program and get access to live sessions, projects, and career coaching.</p>
              <a href="/contact" className="mt-8 inline-flex rounded-full bg-white px-6 py-3 text-sm font-semibold text-slate-950 transition hover:bg-slate-100">Enroll today</a>
            </div>
          </div>

          <div className="grid gap-10 lg:grid-cols-[0.7fr_0.9fr]">
            <div className="space-y-10">
              <div className="space-y-4 rounded-[32px] bg-slate-50 p-8 shadow-sm">
                <SectionTitle eyebrow="Curriculum" title="What you will learn" />
                <ul className="space-y-3 text-slate-600">
                  <li>Modern frontend architecture with React.</li>
                  <li>Backend service design using Node.js and Express.</li>
                  <li>Database modelling with MongoDB.</li>
                  <li>Deployment, CI/CD, and developer tooling.</li>
                </ul>
              </div>
              <div className="rounded-[32px] bg-slate-50 p-8 shadow-sm">
                <SectionTitle eyebrow="Instructor" title="Meet your trainer" />
                <p className="text-slate-600">{course.trainer} is an industry mentor with practical experience building scalable applications and hiring top engineering talent.</p>
              </div>
            </div>

            <div className="space-y-6">
              <div className="rounded-[32px] bg-white p-8 shadow-soft">
                <h3 className="text-xl font-semibold text-slate-900">Benefits</h3>
                <ul className="mt-5 space-y-3 text-slate-600">
                  <li>Live mentoring and feedback loops.</li>
                  <li>Portfolio-worthy capstone project.</li>
                  <li>Verified course certificate.</li>
                  <li>Dedicated career support.</li>
                </ul>
              </div>
              <div className="rounded-[32px] bg-white p-8 shadow-soft">
                <h3 className="text-xl font-semibold text-slate-900">Requirements</h3>
                <ul className="mt-5 space-y-3 text-slate-600">
                  <li>Motivation to learn and build products.</li>
                  <li>Comfortable using a laptop and browser.</li>
                  <li>Basic programming knowledge for intermediate tracks.</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/VerifyCertificate.jsx': '''import { useState } from 'react';
import { useForm } from 'react-hook-form';
import toast from 'react-hot-toast';
import { verifyCertificate } from '../services/certificateService.js';
import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function VerifyCertificate() {
  const { register, handleSubmit, reset } = useForm({ defaultValues: { certificateId: '' } });
  const [result, setResult] = useState(null);
  const [status, setStatus] = useState('idle');

  const onSubmit = async (values) => {
    setStatus('loading');
    try {
      const response = await verifyCertificate(values);
      setResult(response.data);
      toast.success('Certificate verified successfully');
    } catch (error) {
      setResult(null);
      toast.error(error.response?.data?.message || 'Certificate could not be verified');
    } finally {
      setStatus('idle');
      reset();
    }
  };

  return (
    <section className="py-24">
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="grid gap-10 lg:grid-cols-[0.95fr_0.75fr]">
          <div className="space-y-8 rounded-[40px] bg-white p-10 shadow-soft">
            <SectionTitle eyebrow="Verify Certificate" title="Check certificate authenticity in seconds" description="Enter your certificate ID to confirm the student name, course, issue date, and status." />
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
              <label className="block">
                <span className="text-sm font-medium text-slate-900">Certificate ID</span>
                <input {...register('certificateId', { required: true })} type="text" placeholder="NAV-2026-12345" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none transition focus:border-primary" />
              </label>
              <button type="submit" disabled={status === 'loading'} className="btn-gradient">
                {status === 'loading' ? 'Verifying…' : 'Verify Certificate'}
              </button>
            </form>
            {result ? (
              <div className="rounded-[32px] border border-slate-200 bg-slate-50 p-6">
                <p className="text-sm uppercase tracking-[0.3em] text-secondary">Verified</p>
                <div className="mt-4 space-y-3 text-slate-700">
                  <p><strong>Student:</strong> {result.name}</p>
                  <p><strong>Certificate ID:</strong> {result.certificateId}</p>
                  <p><strong>Course:</strong> {result.course}</p>
                  <p><strong>Issue Date:</strong> {result.issueDate}</p>
                  <p><strong>Status:</strong> {result.status}</p>
                </div>
              </div>
            ) : (
              <div className="rounded-[32px] border border-dashed border-slate-200 bg-slate-50 p-6 text-slate-600">
                Please enter a certificate ID to verify its authenticity.
              </div>
            )}
          </div>

          <div className="rounded-[40px] bg-gradient-to-br from-primary to-secondary p-10 text-white shadow-soft">
            <p className="text-sm uppercase tracking-[0.35em] text-white/80">Security first</p>
            <h2 className="mt-4 text-3xl font-semibold">Certificate verification made easy</h2>
            <p className="mt-4 leading-8 text-white/90">Our verification portal helps employers, universities, and learners validate credentials instantly with secure QR and certificate previews.</p>
            <div className="mt-8 space-y-3 text-sm leading-7">
              <p>• Trusted certificate records</p>
              <p>• Real-time authenticity status</p>
              <p>• Secure reporting for every issuance</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/Contact.jsx': '''import { useState } from 'react';
import { useForm } from 'react-hook-form';
import toast from 'react-hot-toast';
import { sendContactMessage } from '../services/contactService.js';
import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function Contact() {
  const { register, handleSubmit, reset } = useForm();
  const [submitting, setSubmitting] = useState(false);

  const onSubmit = async (values) => {
    setSubmitting(true);
    try {
      await sendContactMessage(values);
      toast.success('Message sent successfully');
      reset();
    } catch (error) {
      toast.error(error.response?.data?.message || 'Failed to send message');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section className="py-24">
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="grid gap-10 lg:grid-cols-[0.95fr_0.75fr]">
          <div className="space-y-8 rounded-[40px] bg-white p-10 shadow-soft">
            <SectionTitle eyebrow="Contact" title="Get in touch with our admissions team" description="Share your details and we will recommend the right course, timeline, and scholarship options." />
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
              <div className="grid gap-4 lg:grid-cols-2">
                <label className="block">
                  <span className="text-sm font-medium text-slate-900">Name</span>
                  <input {...register('name', { required: true })} type="text" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none" />
                </label>
                <label className="block">
                  <span className="text-sm font-medium text-slate-900">Phone</span>
                  <input {...register('phone', { required: true })} type="tel" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none" />
                </label>
              </div>
              <div className="grid gap-4 lg:grid-cols-2">
                <label className="block">
                  <span className="text-sm font-medium text-slate-900">Email</span>
                  <input {...register('email', { required: true })} type="email" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none" />
                </label>
                <label className="block">
                  <span className="text-sm font-medium text-slate-900">Subject</span>
                  <input {...register('subject', { required: true })} type="text" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none" />
                </label>
              </div>
              <label className="block">
                <span className="text-sm font-medium text-slate-900">Message</span>
                <textarea {...register('message', { required: true })} rows="5" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm text-slate-900 outline-none" />
              </label>
              <button type="submit" disabled={submitting} className="btn-gradient">
                {submitting ? 'Sending…' : 'Send Message'}
              </button>
            </form>
          </div>

          <aside className="space-y-8 rounded-[40px] bg-gradient-to-br from-primary to-secondary p-10 text-white shadow-soft">
            <div>
              <p className="text-sm uppercase tracking-[0.35em] text-white/80">Company Info</p>
              <h2 className="mt-4 text-3xl font-semibold">Reach us directly</h2>
            </div>
            <div className="space-y-4 text-sm leading-7">
              <p><strong>Address:</strong> 401 Navankur House,  </p>
              <p><strong>Email:</strong> info@navankurra.com</p>
              <p><strong>Phone:</strong> +91 98765 43210</p>
            </div>
            <div className="rounded-3xl bg-white/10 p-6">
              <p className="text-sm uppercase tracking-[0.35em] text-white/80">Working hours</p>
              <p className="mt-3 text-sm leading-7 text-white/90">Mon - Fri: 09:00 AM - 06:00 PM</p>
            </div>
          </aside>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/PrivacyPolicy.jsx': '''import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function PrivacyPolicy() {
  return (
    <section className="py-24">
      <div className="mx-auto max-w-5xl px-6 lg:px-8">
        <SectionTitle eyebrow="Privacy Policy" title="Your privacy matters to us" description="We only collect what is necessary to provide services and to respond to inquiries." />
        <div className="mt-10 space-y-8 rounded-[40px] bg-white p-10 shadow-soft text-slate-700">
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Information we collect</h3>
            <p className="leading-8">We collect personal details such as name, contact, and email when you submit a contact form or request a service.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">How we use data</h3>
            <p className="leading-8">Information is used to respond to inquiries, manage course registration, and improve our services.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Cookie policy</h3>
            <p className="leading-8">We use cookies and analytics to improve site performance and personalize content.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Security</h3>
            <p className="leading-8">We protect your data using standard security measures and never share it with third parties without consent.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/TermsConditions.jsx': '''import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function TermsConditions() {
  return (
    <section className="py-24">
      <div className="mx-auto max-w-5xl px-6 lg:px-8">
        <SectionTitle eyebrow="Terms & Conditions" title="Professional terms for using our platform" description="Please read the conditions carefully before enrolling in any program or submitting personal information." />
        <div className="mt-10 space-y-8 rounded-[40px] bg-white p-10 shadow-soft text-slate-700">
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Acceptance of terms</h3>
            <p className="leading-8">By using Navankurra, you agree to our policies, payment terms, and code of conduct during the learning experience.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Payment and refunds</h3>
            <p className="leading-8">Course fees, schedules, and refund policies are available during registration and may vary by program.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Intellectual property</h3>
            <p className="leading-8">All course content, materials, and branding are owned by Navankurra and are protected by copyright.</p>
          </div>
          <div>
            <h3 className="mb-4 text-2xl font-semibold text-slate-900">Contact us</h3>
            <p className="leading-8">If you have questions about these terms, reach out to info@navankurra.com for clarification.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
''',
    'client/src/pages/NotFound.jsx': '''import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <section className="grid min-h-[calc(100vh-6rem)] place-items-center bg-slate-50 py-24">
      <div className="max-w-2xl rounded-[40px] bg-white p-12 text-center shadow-soft">
        <p className="mb-6 text-sm uppercase tracking-[0.35em] text-secondary">404 error</p>
        <h1 className="text-5xl font-semibold text-slate-950">Page not found</h1>
        <p className="mt-6 text-slate-600">The page you are looking for does not exist or has been moved.</p>
        <Link to="/" className="mt-8 inline-flex rounded-full bg-primary px-6 py-3 text-sm font-semibold text-white transition hover:bg-primary/90">Return home</Link>
      </div>
    </section>
  );
}
''',
    'server/vite.env.example': '',
    'server/package.json': '''{
  "name": "navankur-ra-server",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "nodemon server.js",
    "start": "node server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.3",
    "express-validator": "^7.0.1",
    "helmet": "^7.0.0",
    "jsonwebtoken": "^9.0.2",
    "mongoose": "^7.5.0",
    "mongo-sanitize": "^2.1.0",
    "nodemailer": "^6.9.5"
  },
  "devDependencies": {
    "nodemon": "^3.0.1"
  }
}
''',
    'server/.env.example': '''PORT=5000
MONGO_URI=mongodb://localhost:27017/navankur-ra
JWT_SECRET=replace_with_a_secret_key
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_smtp_user
SMTP_PASS=your_smtp_password
EMAIL_FROM=info@navankurra.com
''',
    'server/server.js': '''import express from 'express';
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
''',
    'server/config/db.js': '''import mongoose from 'mongoose';

const connectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true
    });
    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (error) {
    console.error('MongoDB connection failed:', error.message);
    process.exit(1);
  }
};

export default connectDB;
''',
    'server/config/mailer.js': '''import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT || 587),
  secure: false,
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASS
  }
});

export async function sendEmail({ to, subject, html }) {
  return transporter.sendMail({
    from: process.env.EMAIL_FROM,
    to,
    subject,
    html
  });
}
''',
    'server/models/Course.js': '''import mongoose from 'mongoose';

const CourseSchema = new mongoose.Schema({
  title: { type: String, required: true },
  slug: { type: String, required: true, unique: true },
  description: { type: String, required: true },
  duration: { type: String, required: true },
  mode: { type: String, default: 'Online Live' },
  trainer: { type: String, required: true },
  price: { type: Number, required: true },
  status: { type: String, enum: ['active', 'draft'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.Course || mongoose.model('Course', CourseSchema);
''',
    'server/models/ContactQuery.js': '''import mongoose from 'mongoose';

const ContactQuerySchema = new mongoose.Schema({
  name: { type: String, required: true },
  phone: { type: String, required: true },
  email: { type: String, required: true },
  subject: { type: String, required: true },
  message: { type: String, required: true },
  status: { type: String, enum: ['new', 'read', 'closed'], default: 'new' }
}, { timestamps: true });

export default mongoose.models.ContactQuery || mongoose.model('ContactQuery', ContactQuerySchema);
''',
    'server/models/Certificate.js': '''import mongoose from 'mongoose';

const CertificateSchema = new mongoose.Schema({
  certificateId: { type: String, required: true, unique: true },
  name: { type: String, required: true },
  course: { type: String, required: true },
  issueDate: { type: String, required: true },
  status: { type: String, enum: ['valid', 'revoked'], default: 'valid' }
}, { timestamps: true });

export default mongoose.models.Certificate || mongoose.model('Certificate', CertificateSchema);
''',
    'server/models/Testimonial.js': '''import mongoose from 'mongoose';

const TestimonialSchema = new mongoose.Schema({
  name: { type: String, required: true },
  role: { type: String, required: true },
  review: { type: String, required: true },
  rating: { type: Number, min: 1, max: 5 },
  status: { type: String, enum: ['active', 'hidden'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.Testimonial || mongoose.model('Testimonial', TestimonialSchema);
''',
    'server/models/GalleryItem.js': '''import mongoose from 'mongoose';

const GalleryItemSchema = new mongoose.Schema({
  title: { type: String, required: true },
  imageUrl: { type: String, required: true },
  status: { type: String, enum: ['active', 'hidden'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.GalleryItem || mongoose.model('GalleryItem', GalleryItemSchema);
''',
    'server/models/User.js': '''import mongoose from 'mongoose';

const UserSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  role: { type: String, enum: ['admin', 'staff'], default: 'admin' },
  status: { type: String, enum: ['active', 'inactive'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.User || mongoose.model('User', UserSchema);
''',
    'server/models/FAQ.js': '''import mongoose from 'mongoose';

const FAQSchema = new mongoose.Schema({
  question: { type: String, required: true },
  answer: { type: String, required: true },
  status: { type: String, enum: ['active', 'hidden'], default: 'active' }
}, { timestamps: true });

export default mongoose.models.FAQ || mongoose.model('FAQ', FAQSchema);
''',
    'server/routes/index.js': '''import { Router } from 'express';
import courseRoutes from './courses.js';
import contactRoutes from './contact.js';
import certificateRoutes from './certificate.js';
import authRoutes from './auth.js';
import testimonialRoutes from './testimonials.js';
import galleryRoutes from './gallery.js';

const router = Router();
router.use('/courses', courseRoutes);
router.use('/contact', contactRoutes);
router.use('/certificate', certificateRoutes);
router.use('/auth', authRoutes);
router.use('/testimonials', testimonialRoutes);
router.use('/gallery', galleryRoutes);

router.get('/', (req, res) => res.json({ status: 'ok', message: 'Navankurra API is running' }));

export default router;
''',
    'server/routes/courses.js': '''import { Router } from 'express';
import { body } from 'express-validator';
import { getCourses, getCourseBySlug, createCourse, updateCourse, deleteCourse } from '../controllers/courseController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.get('/', getCourses);
router.get('/:slug', getCourseBySlug);
router.post('/', [body('title').notEmpty(), body('slug').notEmpty(), body('description').notEmpty()], validateRequest, createCourse);
router.put('/:id', [body('title').optional().notEmpty(), body('description').optional().notEmpty()], validateRequest, updateCourse);
router.delete('/:id', deleteCourse);

export default router;
''',
    'server/routes/contact.js': '''import { Router } from 'express';
import { body } from 'express-validator';
import { submitContact } from '../controllers/contactController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/', [
  body('name').notEmpty(),
  body('phone').notEmpty(),
  body('email').isEmail(),
  body('subject').notEmpty(),
  body('message').notEmpty()
], validateRequest, submitContact);

export default router;
''',
    'server/routes/certificate.js': '''import { Router } from 'express';
import { body } from 'express-validator';
import { verifyCertificate } from '../controllers/certificateController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/verify', [body('certificateId').notEmpty()], validateRequest, verifyCertificate);

export default router;
''',
    'server/routes/auth.js': '''import { Router } from 'express';
import { body } from 'express-validator';
import { login } from '../controllers/authController.js';
import validateRequest from '../middleware/validateRequest.js';

const router = Router();
router.post('/login', [body('email').isEmail(), body('password').notEmpty()], validateRequest, login);
export default router;
''',
    'server/routes/testimonials.js': '''import { Router } from 'express';
import { getTestimonials } from '../controllers/testimonialController.js';

const router = Router();
router.get('/', getTestimonials);
export default router;
''',
    'server/routes/gallery.js': '''import { Router } from 'express';
import { getGallery } from '../controllers/galleryController.js';

const router = Router();
router.get('/', getGallery);
export default router;
''',
    'server/controllers/courseController.js': '''import Course from '../models/Course.js';

export const getCourses = async (req, res, next) => {
  try {
    const courses = await Course.find({ status: 'active' }).sort({ createdAt: -1 });
    res.json(courses);
  } catch (error) {
    next(error);
  }
};

export const getCourseBySlug = async (req, res, next) => {
  try {
    const course = await Course.findOne({ slug: req.params.slug, status: 'active' });
    if (!course) return res.status(404).json({ message: 'Course not found' });
    res.json(course);
  } catch (error) {
    next(error);
  }
};

export const createCourse = async (req, res, next) => {
  try {
    const course = await Course.create(req.body);
    res.status(201).json(course);
  } catch (error) {
    next(error);
  }
};

export const updateCourse = async (req, res, next) => {
  try {
    const course = await Course.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!course) return res.status(404).json({ message: 'Course not found' });
    res.json(course);
  } catch (error) {
    next(error);
  }
};

export const deleteCourse = async (req, res, next) => {
  try {
    const course = await Course.findByIdAndDelete(req.params.id);
    if (!course) return res.status(404).json({ message: 'Course not found' });
    res.json({ message: 'Course removed' });
  } catch (error) {
    next(error);
  }
};
''',
    'server/controllers/contactController.js': '''import ContactQuery from '../models/ContactQuery.js';
import { sendEmail } from '../config/mailer.js';

export const submitContact = async (req, res, next) => {
  try {
    const contact = await ContactQuery.create(req.body);
    const html = `
      <h2>New contact inquiry</h2>
      <p><strong>Name:</strong> ${contact.name}</p>
      <p><strong>Phone:</strong> ${contact.phone}</p>
      <p><strong>Email:</strong> ${contact.email}</p>
      <p><strong>Subject:</strong> ${contact.subject}</p>
      <p><strong>Message:</strong> ${contact.message}</p>
    `;
    await sendEmail({ to: process.env.EMAIL_FROM, subject: 'New contact inquiry', html });
    res.status(201).json({ message: 'Contact inquiry saved successfully' });
  } catch (error) {
    next(error);
  }
};
''',
    'server/controllers/certificateController.js': '''import Certificate from '../models/Certificate.js';

export const verifyCertificate = async (req, res, next) => {
  try {
    const certificate = await Certificate.findOne({ certificateId: req.body.certificateId });
    if (!certificate) return res.status(404).json({ message: 'Certificate not found' });
    res.json(certificate);
  } catch (error) {
    next(error);
  }
};
''',
    'server/controllers/authController.js': '''import jwt from 'jsonwebtoken';
import User from '../models/User.js';

export const login = async (req, res, next) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user || req.body.password !== user.password) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }
    const token = jwt.sign({ id: user._id, role: user.role }, process.env.JWT_SECRET, { expiresIn: '7d' });
    res.json({ token, user: { id: user._id, name: user.name, email: user.email, role: user.role } });
  } catch (error) {
    next(error);
  }
};
''',
    'server/controllers/testimonialController.js': '''import Testimonial from '../models/Testimonial.js';

export const getTestimonials = async (req, res, next) => {
  try {
    const items = await Testimonial.find({ status: 'active' }).sort({ createdAt: -1 });
    res.json(items);
  } catch (error) {
    next(error);
  }
};
''',
    'server/controllers/galleryController.js': '''import GalleryItem from '../models/GalleryItem.js';

export const getGallery = async (req, res, next) => {
  try {
    const items = await GalleryItem.find({ status: 'active' }).sort({ createdAt: -1 });
    res.json(items);
  } catch (error) {
    next(error);
  }
};
''',
    'server/middleware/errorHandler.js': '''export default function errorHandler(err, req, res, next) {
  console.error(err);
  const status = err.status || 500;
  res.status(status).json({ message: err.message || 'Server error' });
}
''',
    'server/middleware/rateLimiter.js': '''import rateLimit from 'express-rate-limit';

const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 100,
  standardHeaders: true,
  legacyHeaders: false
});

export default limiter;
''',
    'server/middleware/validateRequest.js': '''import { validationResult } from 'express-validator';

export default function validateRequest(req, res, next) {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ message: 'Validation failed', errors: errors.array() });
  }
  next();
}
'''
}

for path, content in files.items():
    fp = Path(path)
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(content, encoding='utf-8')
print('created', len(files), 'files')
