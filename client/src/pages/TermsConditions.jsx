import SectionTitle from '../components/ui/SectionTitle.jsx';

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
