import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.dev import config as dev_config 
from config.prod import config as prod_config


# Load the appropriate configuration
if os.getenv("ENV", "development") == "production":
    DATABASE_URL = prod_config.DATABASE_URL
else:
    DATABASE_URL = dev_config.DATABASE_URL

# Synchronouse engine
engine = create_engine(DATABASE_URL)

# Synchronous Session maker to be used in FastAPI
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
