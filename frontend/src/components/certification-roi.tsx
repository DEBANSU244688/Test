const courses = [
  {
    title: "AWS Cloud Practitioner",
    provider: "Coursera",
    duration: "6 weeks",
    roi: 9.1,
    note: "Best balance of demand and time-to-skill",
    best: true
  },
  {
    title: "System Design Essentials",
    provider: "Educative",
    duration: "8 weeks",
    roi: 8.7,
    note: "High interview relevance for backend roles",
    best: false
  },
  {
    title: "Advanced SQL for Analytics",
    provider: "NPTEL",
    duration: "4 weeks",
    roi: 8.2,
    note: "Quick boost for data-heavy job descriptions",
    best: false
  }
];

export function CertificationROI() {
  return (
    <section className="rounded-xl border border-slate-700 bg-surface p-6">
      <h3 className="text-lg font-semibold">Certification ROI Comparison</h3>
      <p className="mt-1 text-sm text-slate-300">Compare learning options by ROI and time-to-skill.</p>

      <div className="mt-4 grid gap-3 md:grid-cols-3">
        {courses.map((course) => (
          <article
            key={course.title}
            className={`rounded-lg border p-4 ${course.best ? "border-primary bg-primary/10" : "border-slate-600 bg-background"}`}
          >
            <p className="text-sm font-semibold">{course.title}</p>
            <p className="mt-1 text-xs text-slate-300">Provider: {course.provider}</p>
            <p className="mt-1 text-xs text-slate-300">Duration: {course.duration}</p>
            <p className="mt-2 text-sm font-semibold text-accent">ROI: {course.roi}/10</p>
            <p className="mt-1 text-xs text-slate-300">{course.note}</p>
            {course.best ? <p className="mt-2 text-xs font-semibold text-primary">★ Best choice</p> : null}
          </article>
        ))}
      </div>
    </section>
  );
}
