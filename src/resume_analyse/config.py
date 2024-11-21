from pydantic_settings import BaseSettings

class ResumeAnalyseConfig(BaseSettings):
    MODEL_NAME: str = "gpt-4o"
    CV_UPLOAD_DIR: str = "./resume/"


resume_analyse_config = ResumeAnalyseConfig()