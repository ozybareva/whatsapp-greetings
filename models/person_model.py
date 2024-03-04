from pydantic import Field, BaseModel
from datetime import date


class PersonModel(BaseModel):
    wa_id: str | None
    name: str
    birth_date: date
    phone_number: str
