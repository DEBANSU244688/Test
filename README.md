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
- Backend `/api/health`, `/api/resume/parse`, `/api/match/score`, `/api/heatmap/data`, `/api/roadmap/generate`, `/api/counsellor/chat`, and `/api/recommendations/courses` endpoints
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
