const heatmapData = [
  { skill: "Python", level: "Strong", score: 85, demand: 1.0 },
  { skill: "SQL", level: "Moderate", score: 70, demand: 0.9 },
  { skill: "FastAPI", level: "Moderate", score: 62, demand: 0.8 },
  { skill: "System Design", level: "Weak", score: 45, demand: 0.95 },
  { skill: "Docker", level: "Weak", score: 55, demand: 0.85 },
  { skill: "Cloud (AWS)", level: "Weak", score: 40, demand: 0.92 }
];

function getCellColor(score: number): string {
  if (score >= 75) return "bg-success/40 border-success";
  if (score >= 60) return "bg-warning/30 border-warning";
  return "bg-danger/30 border-danger";
}

export function SkillHeatmap() {
  return (
    <section className="rounded-xl border border-slate-700 bg-surface p-6">
      <h3 className="text-lg font-semibold">Skill Heatmap</h3>
      <p className="mt-1 text-sm text-slate-300">Demand-weighted view of your current skill strengths and gaps.</p>

      <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {heatmapData.map((item) => (
          <article
            key={item.skill}
            title={`${item.skill}: ${item.score}% (${item.level})`}
            className={`rounded-lg border p-4 ${getCellColor(item.score)}`}
          >
            <p className="text-sm font-semibold">{item.skill}</p>
            <p className="mt-1 text-xs text-slate-100">Level: {item.level}</p>
            <p className="mt-1 text-xs text-slate-100">Score: {item.score}%</p>
            <p className="mt-1 text-xs text-slate-100">Demand weight: {item.demand}</p>
          </article>
        ))}
      </div>
    </section>
  );
}
