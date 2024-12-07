from pydantic_settings import BaseSettings
import os

class DevelopmentConfig(BaseSettings):
    DATABASE_URL: str 
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        extra = "allow"
    
config = DevelopmentConfig()
