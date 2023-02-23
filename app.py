from fastapi import FastAPI
# from v1.scripts.create_tables import create_tables

from v1.routes.user_router import router as user_router

app = FastAPI()

app.include_router(user_router)
@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}


