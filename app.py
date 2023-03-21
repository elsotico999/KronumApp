from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from v1.scripts.create_tables import create_tables

from v1.routes.user_router import router as user_router
from v1.routes.country_router import router as country_router
from v1.routes.league_router import router as league_router
from v1.routes.match_router import router as match_router
app = FastAPI()

origins = [
    "*"
]


app.add_middleware (
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)


@app.get('/')
def home():
    return {"message": "Tonto el que lo lea"}

app.include_router(user_router)
app.include_router(country_router)
app.include_router(league_router)
app.include_router(match_router)


