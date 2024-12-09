from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Any
from contextlib import asynccontextmanager

from .database import get_db, engine
from .models import BankmobileFormSubmission, SchoolFormSubmission, Base
from .schemas import FormSubmissionCreate, FormSubmissionOutput
from config.prod import config as prod_config
from config.dev import config as dev_config
import os


# Load the appropriate config
if os.getenv("ENV", "development") == "production":
    config = prod_config
else:
    config = dev_config

    
# Custom lifespan manager using contextlib's asynccontextmanager (even if it's synchronous here)
@asynccontextmanager
async def lifespan_(app: FastAPI):
    #  Startup: Create tables if they don't exist
    print("Starting up: Connecting to the database.")
    Base.metadata.create_all(bind=engine)
    
    # Yield control to FastAPI to process the request
    yield 
    
    # Shutdown: Disposing of the database connection.
    print("Shutting down: Disposing of the database connection.")
    engine.dispose()
    

# FastAPI app with lifespan context manager for startup and shutdown
app = FastAPI(lifespan=lifespan_)
    
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500", 
        "https://itdesktopforms.com",
        "https://main.d31sjm3cbpao3l.amplifyapp.com/",
    ],  # Allow your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


    
# Route to get all form submissions 
@app.get("/bankmobile-submissions/", response_model=List[FormSubmissionOutput])
def form_responses(
        name: str = Query(None), 
        current_school_email: str = Query(None),
        db: Session = Depends(get_db)
        ):
    query = db.query(BankmobileFormSubmission)
    
    if name:
        query = query.filter(BankmobileFormSubmission.name.ilike(f"%{name}%"))
    if current_school_email:
        query = query.filter(BankmobileFormSubmission.current_school_email.ilike(f"%{current_school_email}%"))
      
    return query.all() 


# Route to get all form submissions 
@app.get("/school-submissions/", response_model=List[FormSubmissionOutput])
def form_responses(
        name: str = Query(None), 
        current_school_email: str = Query(None),
        db: Session = Depends(get_db)
        ):
    query = db.query(SchoolFormSubmission)
    
    if name:
        query = query.filter(SchoolFormSubmission.name.ilike(f"%{name}%"))
    if current_school_email:
        query = query.filter(SchoolFormSubmission.current_school_email.ilike(f"%{current_school_email}%"))
      
    return query.all() 


# Route to get a specific form submission by ID
@app.get("/bankmobile-form/{form_id}", response_model=FormSubmissionOutput)
def get_form(form_id: int, db: Session = Depends(get_db)):
    form = db.query(BankmobileFormSubmission).filter(BankmobileFormSubmission.id == form_id).first()  # Synchronous query
    if form:
        return form
    return {"error": "Form not found"}

# Route to get a specific form submission by ID
@app.get("/school-form/{form_id}", response_model=FormSubmissionOutput)
def get_form(form_id: int, db: Session = Depends(get_db)):
    form = db.query(SchoolFormSubmission).filter(SchoolFormSubmission.id == form_id).first()  # Synchronous query
    if form:
        return form
    return {"error": "Form not found"}


# Route to create a form submission instance 
@app.post("/bankmobile-forms/", response_model=FormSubmissionOutput)
def create_form_submission(form: FormSubmissionCreate, db: Session = Depends(get_db)):
    submission = BankmobileFormSubmission(**form.model_dump())
    db.add(submission) # Add to the session
    db.commit() # Commit the transaction
    db.refresh(submission) # Refresh to get the ID and updated values
    return submission


# Route to create a form submission instance 
@app.post("/school-forms/", response_model=FormSubmissionOutput)
def create_form_submission(form: FormSubmissionCreate, db: Session = Depends(get_db)):
    submission = SchoolFormSubmission(**form.model_dump())
    db.add(submission) # Add to the session
    db.commit() # Commit the transaction
    db.refresh(submission) # Refresh to get the ID and updated values
    return submission