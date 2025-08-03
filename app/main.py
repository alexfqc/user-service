from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal

# Create all tables in the database (only for dev/test purposes)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a new database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db  # provides the db session
    finally:
        db.close()  # ensures the session is always closed

@app.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> schemas.UserResponse:
    # Check if a user with the same email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create a new User instance
    new_user = models.User(name=user.name, email=user.email)
    
    # Add to session, commit transaction, and refresh to get the generated ID
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Return the created user (validated with UserResponse schema)
    return new_user
