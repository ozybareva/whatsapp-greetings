from pydantic import Field, BaseModel
from datetime import date


class PersonModel(BaseModel):
    wa_id: str | None
    name: str | None
    birth_date: date | None = None
    phone_number: str | None
