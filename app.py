from fastapi import FastAPI
# from v1.scripts.create_tables import create_tables

from v1.routes.user_router import router as user_router
from v1.routes.country_router import router as country_router
app = FastAPI()

app.include_router(user_router)
app.include_router(country_router)
@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}


