export default function SectionTitle({ eyebrow, title, description }) {
  return (
    <div className="max-w-2xl space-y-3">
      {eyebrow && <p className="text-sm font-semibold uppercase tracking-[0.28em] text-secondary">{eyebrow}</p>}
      <h2 className="text-3xl font-semibold text-slate-900 sm:text-4xl">{title}</h2>
      {description && <p className="text-slate-600">{description}</p>}
    </div>
  );
}
