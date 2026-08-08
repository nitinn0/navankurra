import { motion } from 'framer-motion';
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
