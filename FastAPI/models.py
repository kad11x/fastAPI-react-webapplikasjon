from pydantic import BaseModel, Field
from typing import List, Optional


class User(BaseModel):
    id_User: Optional[int] = Field(None, alias="id_User")
    user_Password: str
    user_Name: str
    user_Email: str

    class Config:
        orm_mode = True


class Exercise(BaseModel):
    id_Exercise: Optional[int] = Field(None, alias="id_Exercise")
    exercise_Name: str
    exercise_Info: str

    class Config:
        orm_mode = True


class Template(BaseModel):
    id_Template: Optional[int] = Field(None, alias="id_Template")
    template_name: str
    user_idUser: int

    class Config:
        orm_mode = True


class ExerciseSet(BaseModel):
    id_Set: Optional[int] = Field(None, alias="id_Set")
    set_Kg: str
    set_Reps: str
    Exercise_idExercise: int
    Template_idTemplate: int

    class Config:
        orm_mode = True


# Example of how to use these models
user_data = {
    "user_Password": "password123",
    "user_Name": "John Doe",
    "user_Email": "john.doe@example.com",
}

user = User(**user_data)
print(user)
