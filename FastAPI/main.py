from fastapi import FastAPI, Depends, HTTPException
from database import *  # Importer create_tables-funksjonen and con
from models import *
from routers import user_router

# testing av sikkerheten:
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

create_tables()

app = FastAPI()

app.include_router(user_router.router)


# Dine importerte filer og modeller
from models import (
    User,
    UserLogin,
    Token,
    TokenData,
)  # Importer modeller fra din models.py-fil

SECRET_KEY = "test"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPPIRES_MINUTS = 30

# Passord krypteringsinnstillinger
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# vertifiserer passordet som er opgitt med heshet passord
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO user (user_Password, userName, user_fierstName, user_Lastname, user_Email)
        VALUES (?, ?, ?)
    """,
        (user_Password, userName, user_Fierstname, user_Lastname, user_Email),
    )
    db.commit()

    # Print statement to show the added user details
    print(
        f"Added user: Password={user_Password}, Name={userName},Name={user_Fierstname},Name={user_Lastname}, Email={user_Email}"
    )
    return UserInDB(**user_data)


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user
