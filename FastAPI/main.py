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
    cursor.execute("SELECT * FROM user WHERE userName = ?", (username,))
    row = cursor.fetchone()
    if row:
        return {
            "id_User": row["id_User"],
            "hashed_user_Password": row["user_hashed_Password"],
            "userName": row["userName"],
            "user_Fierstname": row["user_Fierstname"],
            "user_Lastname": row["user_Lastname"],
            "user_Email": row["user_Email"],
        }
    return None


def authenticate_user(db, username: str, password: str):
    user_data = get_user(db, username)
    if not user_data:
        return False
    if not verify_password(password, user_data["hashed_user_Password"]):
        return False

    # Convert the dictionary back into a User model
    user = User(**user_data)
    return user


db = get_database_connection()
username = "test_user"
password = "password123"
hashed_password = get_password_hash(password)

cursor = db.cursor()
cursor.execute(
    """
INSERT INTO user (user_hashed_Password, userName, user_Fierstname, user_Lastname, user_Email)
 VALUES (?, ?, ?, ?, ?)
""",
    (hashed_password, username, "Test", "User", "test_user@example.com"),
)
db.commit()

# Authenticate the user
user = authenticate_user(db, username, "password123")
if user:
    print("Authentication successful!")
    print(user)
else:
    print("Authentication failed!")
