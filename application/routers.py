import logging
from datetime import date
from models.person_model import PersonModel
from persistance.people_repository import PeopleRepository
from fastapi.responses import JSONResponse


class PersonRouter:

    def __init__(self, repository: PeopleRepository) -> None:
        self.repository = repository

    async def load_new_person(
            self,
            name: str,
            birth_date: date,
            phone_number: str
    ):
        try:
            await self.repository.create_new_person(PersonModel(name=name, birth_date=birth_date, phone_number=phone_number))
            return JSONResponse({'Status': 'Success'})
        except Exception as exc:
            logging.error(f'Error {exc}')
            return JSONResponse({'Status': 'Error'})

