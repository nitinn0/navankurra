import SectionTitle from '../components/ui/SectionTitle.jsx';

export default function About() {
  return (
    <section className="bg-slate-50 py-24">
      <div className="mx-auto max-w-6xl px-6 lg:px-8">
        <div className="rounded-[40px] bg-white p-10 shadow-soft">
          <SectionTitle eyebrow="About Us" title="We help learners build modern careers through immersive education." description="Navankurra brings curated live programs, expert mentoring, and real-world certification to ambitious learners." />

          <div className="mt-16 grid gap-8 lg:grid-cols-[0.95fr_0.85fr] lg:items-start">
            <div className="space-y-8">
              <div className="space-y-4 rounded-3xl border border-slate-200 bg-slate-50 p-7">
                <h3 className="text-xl font-semibold text-slate-900">Our story</h3>
                <p className="text-slate-600 leading-8">Founded to make premium technical training accessible, we blend practical coursework with mentorship, guided practice, and placement support.</p>
              </div>

              <div className="grid gap-4 sm:grid-cols-2">
                <div className="rounded-3xl bg-white p-7 shadow-sm">
                  <h4 className="font-semibold text-slate-900">Mission</h4>
                  <p className="mt-3 text-slate-600">Empower learners with relevant skills, real projects, and a direct path to career growth.</p>
                </div>
                <div className="rounded-3xl bg-white p-7 shadow-sm">
                  <h4 className="font-semibold text-slate-900">Vision</h4>
                  <p className="mt-3 text-slate-600">Create a trusted education brand known for outcomes, innovation, and learner-first experiences.</p>
                </div>
              </div>
            </div>

            <div className="space-y-8">
              <div className="rounded-[32px] bg-gradient-to-br from-primary to-secondary p-8 text-white shadow-soft">
                <p className="text-sm uppercase tracking-[0.3em] text-white/80">Founder message</p>
                <h3 className="mt-5 text-3xl font-semibold">“Every learner deserves a modern education journey that leads to real results.”</h3>
                <p className="mt-4 text-slate-100 leading-8">We combine faculty expertise, live interaction, and career coaching to make the next step clear and achievable.</p>
              </div>
              <div className="grid gap-4 sm:grid-cols-2">
                {['Value-driven curriculum', 'Industry mentors', 'Project-based training', 'Career support'].map((item) => (
                  <div key={item} className="rounded-3xl bg-slate-50 p-6 shadow-sm">
                    <p className="font-semibold text-slate-900">{item}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
