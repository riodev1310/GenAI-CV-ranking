from fastapi import APIRouter, UploadFile, File
from src.resume_analyse import services

router = APIRouter()


@router.post("/analyse")
async def resume_analyse_router(file: UploadFile = File(...)):
    file_name = await services.save_cv_candidate(file=file)
    
    cv_contents = services.read_cv_candidate(file_name=file_name)
    
    strengths = services.analysing_strength(cv_contents)
    
    weakness = services.analysing_weakness(cv_contents)
    
    return strengths, weakness