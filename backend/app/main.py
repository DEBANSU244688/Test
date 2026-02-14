from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger

from app.api.health import router as health_router
from app.api.resume import router as resume_router
from app.api.match import router as match_router
from app.api.heatmap import router as heatmap_router
from app.api.roadmap import router as roadmap_router
from app.api.counsellor import router as counsellor_router
from app.api.recommendations import router as recommendations_router
<<<<<<< HEAD
=======
from app.api.job import router as job_router
from app.api.skills import router as skills_router
from app.api.gap import router as gap_router
>>>>>>> origin/Main

app = FastAPI(
    title="Career Path Optimizer API",
    version="0.2.0",
    description="Backend APIs for resume parsing, matching, and career recommendations.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("Incoming request: {} {}", request.method, request.url.path)
    response = await call_next(request)
    logger.info("Response status: {} for {}", response.status_code, request.url.path)
    return response


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled error on {}: {}", request.url.path, exc)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


app.include_router(health_router, prefix="/api")
app.include_router(resume_router, prefix="/api")
app.include_router(match_router, prefix="/api")
app.include_router(heatmap_router, prefix="/api")
app.include_router(roadmap_router, prefix="/api")
app.include_router(counsellor_router, prefix="/api")
app.include_router(recommendations_router, prefix="/api")
<<<<<<< HEAD
=======
app.include_router(job_router, prefix="/api")
app.include_router(skills_router, prefix="/api")
app.include_router(gap_router, prefix="/api")
>>>>>>> origin/Main


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Career Path Optimizer backend is running"}
