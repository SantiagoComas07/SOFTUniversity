
from sqlmodel import create_engine, SQLModel
from ..config import postgres_url
from ..models import UserBase

# CREATE THE DATABASE ENGINE
engine = create_engine(postgres_url, echo=True)

#CREATE THE FUNCTION TO SYNCRONIZE THE DATABASE 

def init_db():
    SQLModel.metadata.create_all(engine)