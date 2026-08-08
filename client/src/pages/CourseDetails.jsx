import { useEffect, useState } from 'react';
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
