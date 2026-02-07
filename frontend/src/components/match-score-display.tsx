const breakdown = [
  { label: "Skills", value: 78, color: "text-success" },
  { label: "Tools", value: 65, color: "text-warning" },
  { label: "Experience", value: 72, color: "text-accent" }
];

export function MatchScoreDisplay() {
  const score = 74;

  return (
    <section className="grid gap-4 rounded-xl border border-slate-700 bg-surface p-6 md:grid-cols-2">
      <div className="flex items-center gap-4">
        <div className="flex h-32 w-32 items-center justify-center rounded-full border-8 border-primary text-3xl font-bold text-primary">
          {score}%
        </div>
        <div>
          <h3 className="text-lg font-semibold">Match Score</h3>
          <p className="text-sm text-slate-300">Overall resume fit against selected role.</p>
        </div>
      </div>

      <div>
        <h4 className="text-sm font-semibold uppercase tracking-wide text-slate-300">Breakdown</h4>
        <ul className="mt-2 space-y-2">
          {breakdown.map((item) => (
            <li key={item.label} className="flex items-center justify-between rounded-md border border-slate-600 px-3 py-2">
              <span>{item.label}</span>
              <span className={`font-semibold ${item.color}`}>{item.value}%</span>
            </li>
          ))}
        </ul>
        <div className="mt-4 rounded-md border border-slate-600 bg-background p-3 text-sm text-slate-300">
          <p className="font-semibold text-white">Why this score?</p>
          <p className="mt-1">
            Skills carry the highest weight. Your profile is strongest on core technical skills,
            but tool depth and role-specific experience can be improved.
          </p>
        </div>
      </div>
    </section>
  );
}
