import { useState } from 'react';
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
              <p><strong>Address:</strong> 401 Navankur House, Mumbai, India</p>
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
