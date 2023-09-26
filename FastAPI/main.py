from fastapi import FastAPI
import sellers, buyers
from database import create_tables  # Importer create_tables-funksjonen

app = FastAPI()

app.include_router(buyers.router)
app.include_router(sellers.router)

create_tables()
