from fastapi import APIRouter, Body, UploadFile, File
from src.candidates import services

router = APIRouter()

@router.post("/analyse")
async def analyse_candidate_router(file: UploadFile = File(...)):
    file_name = await services.save_cv_candidate(file=file)
    cv_content = services.read_cv_candidate(file_name=file_name)
    analysis = services.analyse_candidate(cv_content=cv_content)
    return analysis