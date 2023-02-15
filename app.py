from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}


