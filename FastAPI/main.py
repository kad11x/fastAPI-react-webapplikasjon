from fastapi import FastAPI
from database import *  # Importer create_tables-funksjonen and con

get_database_connection()

create_tables()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
