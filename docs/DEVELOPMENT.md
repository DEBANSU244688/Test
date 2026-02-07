# Development Guide

## Prerequisites
- Node.js 20+
- Python 3.11+
- Docker (optional)

## Local startup

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

## Tests
```bash
cd backend
pytest
```
