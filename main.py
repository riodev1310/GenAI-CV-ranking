from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from src.candidates.routers import router as candidate_router
from src.jobs.routers import router as job_router


app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Message": "Welcome Bot CV Ranking"}

@app.get("/healthz")
async def healthcheck() -> bool:
    return True

app.include_router(candidate_router, prefix="/candidate", tags=["Candidate"])
app.include_router(job_router, prefix="/job", tags=["Job"])