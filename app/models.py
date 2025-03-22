

from sqlalchemy import Column, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    username_length = Column(Integer, nullable=False)
    num_digits_in_username = Column(Integer, nullable=False)
    profile_completeness = Column(Integer, nullable=False)
    activity_score = Column(Integer, nullable=False)
    avg_posts_per_day = Column(Float, nullable=False)
    avg_likes_per_post = Column(Float, nullable=False)
    num_hashtags_used = Column(Integer, nullable=False)
    num_mentions_used = Column(Integer, nullable=False)
    account_privacy = Column(Boolean, nullable=False)
    profile_has_bio = Column(Boolean, nullable=False)
    profile_has_picture = Column(Boolean, nullable=False)
    suspicious_words_in_bio = Column(Integer, nullable=False)
    engagement_rate = Column(Float, nullable=False)
    friend_follower_ratio = Column(Float, nullable=False)
    spam_word_count = Column(Integer, nullable=False)
    bio_sentiment_score = Column(Float, nullable=True)  # ✅ Add this field
    bio_word_count = Column(Integer, nullable=False)
    time_gap_variance = Column(Float, nullable=False)
    last_seen_days_ago = Column(Integer, nullable=False)
    status = Column(Integer, nullable=True)  # ✅ Add this field