from fastapi import FastAPI, Depends, HTTPException, APIRouter
from database import *  # Importer create_tables-funksjonen and con
from services import user_service
from models import *

create_tables()

router = APIRouter(
    prefix="/user",
)


@router.post("/users/", response_model=User)
def create_user(user: User, db=Depends(get_db)):
    user_service.add_user(
        user.hashed_user_Password,
        user.user_Name,
        user.user_Fierstname,
        user.user_Lastname,
        user.user_Email,
        db,
    )
    return user


@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db=Depends(get_db)):
    user_service.delete_user(user_id, db)
    return {"message": "User deleted successfully"}
