const roadmap = [
  { month: "Month 1", skill: "Python & DSA", milestone: "40 interview problems", cert: "NPTEL Problem Solving", progress: 15 },
  { month: "Month 2", skill: "SQL & Data Modeling", milestone: "Analytics mini-project", cert: "Coursera SQL for Data Science", progress: 10 },
  { month: "Month 3", skill: "Backend APIs", milestone: "3 FastAPI endpoints", cert: "FastAPI Advanced Concepts", progress: 8 },
  { month: "Month 4", skill: "System Design", milestone: "2 system design case studies", cert: "Grokking System Design", progress: 5 },
  { month: "Month 5", skill: "Cloud Deployment", milestone: "Deploy full-stack app", cert: "AWS Cloud Practitioner", progress: 0 },
  { month: "Month 6", skill: "Interview Readiness", milestone: "Mock interview cycle", cert: "Interview Masterclass", progress: 0 }
];

export function LearningRoadmap() {
  return (
    <section className="rounded-xl border border-slate-700 bg-surface p-6">
      <h3 className="text-lg font-semibold">6-Month Learning Roadmap</h3>
      <p className="mt-1 text-sm text-slate-300">Month-wise milestones with certifications and progress tracking.</p>

      <div className="mt-4 grid gap-3 md:grid-cols-2">
        {roadmap.map((item) => (
          <article key={item.month} className="rounded-lg border border-slate-600 bg-background p-4">
            <p className="text-sm font-semibold text-accent">{item.month}</p>
            <p className="mt-1 text-sm font-medium">{item.skill}</p>
            <p className="mt-1 text-xs text-slate-300">Milestone: {item.milestone}</p>
            <p className="mt-1 text-xs text-slate-300">Certification: {item.cert}</p>
            <div className="mt-2 h-2 w-full rounded-full bg-slate-700">
              <div className="h-2 rounded-full bg-primary" style={{ width: `${item.progress}%` }} />
            </div>
            <p className="mt-1 text-right text-xs text-slate-400">{item.progress}% complete</p>
          </article>
        ))}
      </div>
    </section>
  );
}
