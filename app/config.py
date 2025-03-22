import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://fastapi_user:password123@localhost/fake_profiles")
