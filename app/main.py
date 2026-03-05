from fastapi import FastAPI
from .src.db import init_db

def lifespan(app):
    init_db()
    yield
    print("The server is down")



# Run the Server
app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Hello world"}