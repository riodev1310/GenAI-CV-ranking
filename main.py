from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings


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
