from models.person_model import PersonModel
from persistance.mongo_connection import MongoConnector
from persistance.repository import Repository
from settings.settings import Settings


class PeopleRepository(Repository):
    def __init__(self, mongo: MongoConnector, settings: Settings):
        super().__init__(mongo, settings)

    def collection_name(self) -> str:
        return 'people'

    async def create_new_person(self, person: PersonModel):
        await self.save_data(person.model_dump())
