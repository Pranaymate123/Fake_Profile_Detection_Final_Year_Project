from sqlalchemy import Column, Integer, String
from app.database import Base, engine

# Define TestProfile Table
class TestProfile(Base):
    __tablename__ = "test_profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# Create Table in the Database
Base.metadata.create_all(bind=engine)
