from pydantic import BaseModel, Field
from typing import List, Optional


# user generel user
class User(BaseModel):
    id_User: Optional[int] = Field(None, alias="id_User")
    hashed_user_Password: str
    userName: str
    user_Fierstname: str
    user_Lastname: str
    user_Email: str


# user login class
class UserLogin(BaseModel):
    user_Password: str
    userName: str


class Exercise(BaseModel):
    id_Exercise: Optional[int] = Field(None, alias="id_Exercise")
    exercise_Name: str
    exercise_Info: str


class Template(BaseModel):
    id_Template: Optional[int] = Field(None, alias="id_Template")
    template_name: str
    user_idUser: int


class ExerciseSet(BaseModel):
    id_Set: Optional[int] = Field(None, alias="id_Set")
    set_Kg: str
    set_Reps: str
    Exercise_idExercise: int
    Template_idTemplate: int


# authentication classes->


class Token(BaseModel):
    accesse_token: str
    token_type: str


class TokenData(BaseModel):
    userName: str


"""# Example of how to use these models
user_data = {
    "id_User": "1",
    "user_Password": "password123",
    "user_Name": "John Doe",
    "user_Email": "john.doe@example.com",
}

user = User(**user_data)
print(user)"""
