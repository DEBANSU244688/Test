import { DashboardLayout } from "@/components/dashboard-layout";
import { ResumeAnalysis } from "@/components/resume-analysis";
import { MatchScoreDisplay } from "@/components/match-score-display";
import { ThemeToggle } from "@/components/theme-toggle";
import { SkillHeatmap } from "@/components/skill-heatmap";
import { LearningRoadmap } from "@/components/learning-roadmap";
import { AICounsellor } from "@/components/ai-counsellor";
import { CertificationROI } from "@/components/certification-roi";

const steps = ["Upload your resume", "Add a job description", "Get your skill-gap roadmap"];

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-6xl flex-col gap-8 px-6 py-16">
      <header className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-primary">Career Path Optimizer</h1>
        <ThemeToggle />
      </header>

      <section className="rounded-xl bg-surface p-8 shadow-xl">
        <h2 className="text-2xl font-semibold">Resume-to-Job Match with AI insights</h2>
        <p className="mt-3 text-slate-300">
          Analyze your resume against a target role, discover missing skills, and get an actionable
          6-month learning roadmap.
        </p>
        <button className="mt-6 rounded-md bg-primary px-5 py-2 font-semibold text-slate-950">Upload Resume</button>
      </section>

      <section className="grid gap-4 md:grid-cols-3">
        {steps.map((step, index) => (
          <article className="rounded-lg border border-slate-700 p-5" key={step}>
            <p className="text-sm text-accent">Step {index + 1}</p>
            <p className="mt-2 font-medium">{step}</p>
          </article>
        ))}
      </section>

      <DashboardLayout />
      <ResumeAnalysis />
      <MatchScoreDisplay />
      <SkillHeatmap />
      <LearningRoadmap />
      <AICounsellor />
      <CertificationROI />
    </main>
  );
}
