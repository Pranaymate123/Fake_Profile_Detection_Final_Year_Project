import xgboost as xgb
import pandas as pd
def predict_profile(profile_data):
    # Convert input data to a DataFrame
    df = pd.DataFrame([profile_data])

    # Load the trained model
    model = xgb.Booster()
    model.load_model("models/fake_profile_model.json")

    # Ensure the input data has the expected features
    expected_features = [
        "username_length", "num_digits_in_username", "profile_completeness",
        "activity_score", "avg_posts_per_day", "avg_likes_per_post",
        "num_hashtags_used", "num_mentions_used", "account_privacy",
        "profile_has_bio", "profile_has_picture", "suspicious_words_in_bio",
        "engagement_rate", "friend_follower_ratio", "bio_sentiment_score",
        "bio_word_count", "spam_word_count", "time_gap_variance",
        "last_seen_days_ago"
    ]

    # Ensure only required features are passed
    dmatrix = xgb.DMatrix(df[expected_features])
    probability = model.predict(dmatrix)[0]  # Get first prediction

    # Apply threshold (0.5 is standard, adjust if needed)
    predicted_label = 1 if probability >= 0.5 else 0

    return predicted_label  # Returns 0 (Fake) or 1 (Legit)
