from sqlalchemy.orm import Session
from app.models import Profile


def store_profile(db: Session, profile_data, prediction: int):
    """
    Stores a single predicted profile in the database.

    :param db: Database session
    :param profile_data: Profile request data
    :param prediction: Prediction result (0 = Legit, 1 = Fake)
    :return: Created Profile Object
    """
    new_profile = Profile(
        **profile_data.dict(),  # Extract and map input fields
        status=prediction  # Store the predicted status
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)  # Refresh to get the auto-generated ID

    return new_profile  # Return stored profile
