from fastapi import FastAPI, Depends, HTTPException, APIRouter, Response
from database import *  # Importer create_tables-funksjonen and con
from services import user_service
from models import *

create_tables()


router = APIRouter(
    prefix="/user",
)


@router.post("/", response_model=User)
def create_user(user: User, db=Depends(get_db)):
    user_service.add_user(
        user.user_Password,
        user.userName,
        user.user_Fierstname,
        user.user_Lastname,
        user.user_Email,
        db,
    )
    return user


@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db=Depends(get_db)):
    user_service.delete_user(user_id, db)
    return {"message": "User deleted successfully"}


@router.post("/login/")
def login_user(user: UserLogin, db=Depends(get_db)):
    user_data = user_service.login_user(user.userName, user.user_Password, db)

    if user_data:
        return Response(status_code=200)
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
