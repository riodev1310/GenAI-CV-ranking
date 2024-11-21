from fastapi import APIRouter
from src.jobs import services
from src.jobs.schemas import JobSchema

router = APIRouter()

@router.post("/analyse")
async def analyse_job(job_data: JobSchema):
    job_analysis = services.analyse_job(job_data=job_data)
    
    return job_analysis