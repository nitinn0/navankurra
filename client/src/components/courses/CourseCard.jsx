import { Link } from 'react-router-dom';
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
