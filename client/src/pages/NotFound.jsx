import { Link } from 'react-router-dom';

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
