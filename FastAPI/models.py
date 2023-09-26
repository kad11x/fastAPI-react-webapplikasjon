from pydantic import BaseModel

class Buyer(BaseModel):
    name: str
    email: str

class Seller(BaseModel):
    name: str
    company: str
