import { Link } from 'react-router-dom';

const stats = [
  { label: 'Students Trained', value: '12,500' },
  { label: 'Courses', value: '24' },
  { label: 'Certificates', value: '9,840' },
  { label: 'Contact Queries', value: '68' }
];

export default function AdminDashboard() {
  return (
    <section className="py-24">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mb-10 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.34em] text-secondary">Admin Panel</p>
            <h1 className="mt-3 text-4xl font-semibold text-slate-950">Dashboard</h1>
          </div>
          <Link to="/" className="rounded-full border border-slate-200 px-5 py-3 text-sm font-semibold text-slate-900 hover:bg-slate-100">Live Website</Link>
        </div>

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {stats.map((item) => (
            <div key={item.label} className="rounded-[28px] bg-white p-7 shadow-soft">
              <p className="text-sm uppercase tracking-[0.26em] text-slate-500">{item.label}</p>
              <p className="mt-5 text-3xl font-semibold text-slate-950">{item.value}</p>
            </div>
          ))}
        </div>

        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <div className="rounded-[28px] bg-white p-8 shadow-soft">
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold text-slate-900">Manage Courses</h2>
              <button className="btn-gradient">Add Course</button>
            </div>
            <div className="mt-6 space-y-4">
              <div className="rounded-2xl border border-slate-200 bg-slate-50 p-4">
                <p className="font-semibold text-slate-900">Full Stack Web Development</p>
                <p className="mt-2 text-sm text-slate-500">Online Live • 6 Months</p>
              </div>
              <div className="rounded-2xl border border-slate-200 bg-slate-50 p-4">
                <p className="font-semibold text-slate-900">Data Science Bootcamp</p>
                <p className="mt-2 text-sm text-slate-500">Online Live • 5 Months</p>
              </div>
            </div>
          </div>

          <div className="rounded-[28px] bg-slate-950 p-8 text-white shadow-soft">
            <h2 className="text-xl font-semibold">Contact Queries</h2>
            <div className="mt-6 space-y-4">
              <div className="rounded-2xl border border-white/10 p-4">
                <p className="font-semibold">Admisssion Enquiry</p>
                <p className="mt-2 text-sm text-slate-300">New registration from Mumbai</p>
              </div>
              <div className="rounded-2xl border border-white/10 p-4">
                <p className="font-semibold">Course Query</p>
                <p className="mt-2 text-sm text-slate-300">Interested in Cloud Engineering</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
