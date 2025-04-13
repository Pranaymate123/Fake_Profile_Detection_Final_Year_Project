# General Success Message
SUCCESS = {"code": 200, "message": "Success"}

# Error Codes and Messages
ERRORS = {
    "BAD_REQUEST": {"code": 400, "message": "Invalid request format. Please check the input data"},
    "NOT_FOUND": {"code": 404, "message": "Resource not found."},
    "INTERNAL_ERROR": {"code": 500, "message": "Internal Server Error."},
    "DB_ERROR": {"code": 503, "message": "Database error. Please try again later."},
    "VALIDATION_ERROR": {"code": 422, "message": "Validation failed. Check input data."},

    # Added new error types for fake profile detection
    "FAKE_PROFILE_DETECTION_ERROR": {"code": 422, "message": "Error in fake profile detection process."},
    "PROFILE_STORAGE_ERROR": {"code": 500, "message": "Error storing profile in the database."},
    "PREDICTION_ERROR": {"code": 500, "message": "Error in profile prediction process."},

    # Additional error types could go here
}
