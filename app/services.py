from sqlalchemy.orm import Session
from app.models import Profile
import hashlib

def generate_profile_ref(profile_data):
    """Generate a unique hash for the profile based on its features."""
    profile_str = str(profile_data)  # Convert to string
    return hashlib.md5(profile_str.encode()).hexdigest()  # Generate hash


def store_profile(db: Session, profile_data, status):
    """Store the profile reference and status in the database."""
    profile_ref = generate_profile_ref(profile_data)

    # Check if the profile already exists
    existing_profile = db.query(Profile).filter(Profile.profile_ref == profile_ref).first()
    if existing_profile:
        return existing_profile  # Avoid duplicate insertion

    # Insert new profile
    new_profile = Profile(profile_ref=profile_ref, status=status)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile