export function ResumeAnalysis() {
  return (
    <section className="grid gap-4 rounded-xl border border-slate-700 bg-surface p-6 md:grid-cols-2">
      <div>
        <h3 className="text-lg font-semibold">Resume Analysis</h3>
        <p className="mt-2 text-sm text-slate-300">Upload your resume (PDF/DOCX) and provide a target job description.</p>
      </div>

      <form className="space-y-3">
        <label className="block text-sm">
          Resume file
          <input
            className="mt-1 block w-full rounded-md border border-slate-600 bg-background px-3 py-2"
            type="file"
            accept=".pdf,.doc,.docx"
          />
        </label>
        <label className="block text-sm">
          Job description
          <textarea
            className="mt-1 block min-h-24 w-full rounded-md border border-slate-600 bg-background px-3 py-2"
            placeholder="Paste the target job description"
          />
        </label>
        <div className="flex items-center justify-between">
          <button className="rounded-md bg-primary px-4 py-2 font-semibold text-slate-950" type="submit">
            Analyze Resume
          </button>
          <p className="text-xs text-warning">Status: Ready to process</p>
        </div>
      </form>
    </section>
  );
}
