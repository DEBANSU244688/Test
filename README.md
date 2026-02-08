# Career Path Optimizer

Monorepo for the Resume-to-Job Matcher & Skill Gap Analyzer.

## Structure
- `frontend/` Next.js + TypeScript + Tailwind CSS starter
- `backend/` FastAPI starter APIs
- `docs/` project docs and workflow notes

## Implemented milestones
- Landing page and dashboard shell
- Resume analysis form UI
- Match score visualization card with explanation panel
- Skill heatmap dashboard with demand-weighted tiles
- Learning roadmap timeline with milestone progress
- AI career counsellor chat panel with contextual insights
- Certification ROI comparison cards with best-choice highlighting
- Job parser now returns grouped requirement extraction (must-have/preferred/responsibilities) for richer downstream analysis
- Gap analysis now supports weak-skill detection using optional per-skill proficiency levels
- Gap analysis now surfaces future-proof skills using trend-based ranking for missing high-value skills
- Gap analysis now consumes a market-demand dataset to score trends and drive future-proof recommendations
- Added backend skill-frequency analyzer utility for normalized counting/ranking of extracted skills
- Added role-skill demand matrix builder that combines skill frequency and market demand weighting
- Added market-demand update schedule metadata (weekly cadence) to support periodic data refresh workflows
- Added market-demand analytics summary with Pandas/NumPy path (and deterministic Python fallback)
- Added market data ingestion pipeline utility to aggregate skills from job-post text records
- Gap analysis now returns a derived heatmap data structure (current/target/demand/status) for visualization layers
- Backend `/api/health`, `/api/resume/parse`, `/api/skills/extract`, `/api/match/score`, `/api/gap/analyze`, `/api/heatmap/data`, `/api/roadmap/generate`, `/api/counsellor/chat`, `/api/recommendations/courses`, `/api/job/parse`, and `/api/job/templates` endpoints
- OpenAPI docs available at `/docs` when backend is running

## Quick start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker compose up --build
```
