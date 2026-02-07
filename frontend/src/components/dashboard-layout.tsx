const sections = [
  "Resume Analysis",
  "Match Score",
  "Skill Heatmap",
  "Learning Roadmap",
  "AI Counsellor"
];

export function DashboardLayout() {
  return (
    <section className="rounded-xl border border-slate-700 bg-surface p-6">
      <h2 className="text-xl font-semibold">Dashboard Overview</h2>
      <nav className="mt-4 grid gap-3 md:grid-cols-5">
        {sections.map((section) => (
          <button
            key={section}
            type="button"
            className="rounded-md border border-slate-600 px-3 py-2 text-sm transition hover:border-accent hover:text-accent"
          >
            {section}
          </button>
        ))}
      </nav>
    </section>
  );
}
