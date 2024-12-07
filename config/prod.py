from pydantic_settings import BaseSettings

class ProductionConfig(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
        
    class Config:
        env_file = ".env"
        extra = "allow"
        
config = ProductionConfig()
