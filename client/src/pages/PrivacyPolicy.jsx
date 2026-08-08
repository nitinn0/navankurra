import SectionTitle from '../components/ui/SectionTitle.jsx';

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
