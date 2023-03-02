'''CRUD COUNTRIES'''
from fastapi import HTTPException, status

from ..schema import country_schema
from ..model.country_model import Country 

def get_countries(id: int = None, name:str=None):
    list_countries = []
    countries = Country.filter()

    for c in countries:
        print(c.name)
        list_countries.append(
            country_schema.Country(id=str(c),name=c.name)
        )
    return list_countries