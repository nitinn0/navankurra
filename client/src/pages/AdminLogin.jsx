import { useForm } from 'react-hook-form';
import { Link } from 'react-router-dom';

export default function AdminLogin() {
  const { register, handleSubmit } = useForm();

  const onSubmit = (values) => {
    console.log('Admin login submitted', values);
  };

  return (
    <section className="min-h-[calc(100vh-10rem)] bg-slate-50 py-24">
      <div className="mx-auto max-w-xl px-6">
        <div className="rounded-[40px] bg-white p-10 shadow-soft">
          <div className="mb-8 text-center">
            <span className="inline-flex h-16 w-16 items-center justify-center rounded-3xl bg-gradient-to-br from-primary to-secondary text-white shadow-soft">N</span>
            <h1 className="mt-6 text-3xl font-semibold text-slate-950">Admin Login</h1>
            <p className="mt-4 text-slate-600">Sign in to manage courses, certificates, testimonials, and queries.</p>
          </div>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            <label className="block">
              <span className="text-sm font-medium text-slate-900">Email</span>
              <input {...register('email', { required: true })} type="email" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm outline-none" />
            </label>
            <label className="block">
              <span className="text-sm font-medium text-slate-900">Password</span>
              <input {...register('password', { required: true })} type="password" className="mt-3 w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-4 text-sm outline-none" />
            </label>
            <button type="submit" className="btn-gradient w-full">Login</button>
          </form>
          <div className="mt-6 text-center text-sm text-slate-600">
            <Link to="/" className="text-primary font-semibold">Return to website</Link>
          </div>
        </div>
      </div>
    </section>
  );
}
