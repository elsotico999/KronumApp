'''CRUD COUNTRIES'''
from fastapi import HTTPException, status

from ..schema import country_schema
from ..model.country_model import Country 

def get_countries(id: int, name:str):
    list_countries = []
    if id:
        c = Country.filter(Country.id == id)
        print (c)
        pass