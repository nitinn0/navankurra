import { useState } from 'react';
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
