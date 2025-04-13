from pydantic import BaseModel
from typing import List, Dict, Any, Optional

# Schema for a single profile request
class ProfileRequest(BaseModel):
    username_length: int
    num_digits_in_username: int
    profile_completeness: int
    activity_score: int
    avg_posts_per_day: float
    avg_likes_per_post: float
    num_hashtags_used: int
    num_mentions_used: int
    account_privacy: bool
    profile_has_bio: bool
    profile_has_picture: bool
    suspicious_words_in_bio: int
    engagement_rate: float
    friend_follower_ratio: float
    spam_word_count: int
    bio_sentiment_score: float  # Ensure this exists
    bio_word_count: int         # Ensure this exists
    time_gap_variance: float    # Ensure this exists
    last_seen_days_ago: int     # Ensure this exists

# Schema for bulk profiles request
class BulkProfilesRequest(BaseModel):
    profiles: List[ProfileRequest]

# Success Response Schema for Bulk Predictions
class SuccessResponse(BaseModel):
    status: str = "success"
    code: int
    message: str
    data: List[Dict[str, Any]]  # List of profile predictions

# Error Response Schema
class ErrorResponse(BaseModel):
    status: str = "error"
    code: int
    message: str
    details: Optional[str] = None  # Detailed error message (optional)
