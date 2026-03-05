from sqlmodel import SQLModel, Field
from datetime import datetime


# MODELS

class User(SQLModel, table=True):
    user_id: int | None = Field(default=False, primary_key=True)
    name: str
    email: str
    phone: int


    