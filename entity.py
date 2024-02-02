from datetime import date

from pydantic import BaseModel


class Person(BaseModel):
    person_id: str
    name: str
    birth_date: date | None
    
    class Config:
        orm_mode = True
