from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, test_connection
from app.database import engine
from app.models import Base

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Profile
from app.schemas import BulkProfilesRequest, SuccessResponse, ErrorResponse
from app.predictor import predict_profile
from app.constants import SUCCESS, ERRORS
from app.services import store_profile


app = FastAPI()


# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

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

@app.post("/add-profiles", response_model=SuccessResponse, responses={400: {"model": ErrorResponse}})
def add_profiles(request: BulkProfilesRequest, db: Session = Depends(get_db)):
    try:
        predictions = []

        for profile_data in request.profiles:
            prediction = predict_profile(profile_data.dict())  # Now returns 0 or 1

            # Ensure prediction is directly used (no indexing needed)
            status = int(prediction)  # 0 (Fake) or 1 (Legit)

            # Store the profile in the database immediately
            stored_profile = store_profile(db, profile_data, status)

            # Append results
            predictions.append({
                "id": stored_profile.id,
                "prediction": "Fake" if status == 0 else "Legit"
            })

        return SuccessResponse(
            code=SUCCESS["code"],
            message="Profiles processed and stored successfully!",
            data=predictions
        )

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=ErrorResponse(
                code=ERRORS["INTERNAL_ERROR"]["code"],
                message=ERRORS["INTERNAL_ERROR"]["message"],
                details=str(e)
            ).dict()
        )
