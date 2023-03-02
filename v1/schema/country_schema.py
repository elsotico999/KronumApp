from pydantic import BaseModel ,Field 
from typing import Optional
# from pydantic import Field

class CountryBase(BaseModel):
    name: Optional[str] = Field (
        ...,
        min_length=3,
        max_length=20,
        exemple="Muy muy lejano"
    )
class Country(CountryBase):
    id: Optional[int] = Field(...,example="12",)
    
