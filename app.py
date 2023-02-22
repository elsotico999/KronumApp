from fastapi import FastAPI
from v1.utils import db


app = FastAPI()


@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}


