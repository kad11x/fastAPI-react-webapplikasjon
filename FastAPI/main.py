from fastapi import FastAPI, Depends, HTTPException
from database import *  # Importer create_tables-funksjonen and con
from models import *
from routers import user_router

create_tables()

app = FastAPI()

app.include_router(user_router.router)
