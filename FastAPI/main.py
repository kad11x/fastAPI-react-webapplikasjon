from fastapi import FastAPI, Depends, HTTPException
from database import *  # Importer create_tables-funksjonen and con
from services import user_service
from models import *

create_tables()

app = FastAPI()


# Dependency
def get_db():
    db = get_database_connection()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: User, db=Depends(get_db)):
    user_service.add_user(user.user_Password, user.user_Name, user.user_Email, db)
    return user


@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db=Depends(get_db)):
    user_service.delete_user(user_id, db)
    return {"message": "User deleted successfully"}


@app.get("/")
def read_root():
    return {"Hello": "World"}
