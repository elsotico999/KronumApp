from pydantic import BaseModel
from pydantic import Field

class CountryBase(BaseModel):
    name: str = Field (
        ...,
        min_length=3,
        max_length=20,
        exemple="Muy muy lejano"
    )
class Country(CountryBase):
    id: int = Field(...,example="12")
