from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, test_connection
from app.models import TestProfile

app = FastAPI()

# Define Pydantic Model for Request Body
class ProfileRequest(BaseModel):
    name: str
    email: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "FastAPI with MySQL - Fake Profiles DB"}

@app.get("/test-db")
def test_db_connection():
    try:
        test_connection()
        return {"status": "success", "message": "Database connected!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/add-profile")
def add_profile(profile: ProfileRequest, db: Session = Depends(get_db)):
    new_profile = TestProfile(name=profile.name, email=profile.email)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return {"status": "success", "message": "Profile added successfully!", "profile": {"id": new_profile.id, "name": new_profile.name, "email": new_profile.email}}
