from fastapi import FastAPI
from v1.scripts.create_tables import create_tables

create_tables()
app = FastAPI()


@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}


