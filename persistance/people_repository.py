from persistance.mongo_connection import MongoConnector
from persistance.repository import Repository
from settings.settings import Settings


class PeopleRepository(Repository):
    def __init__(self, MongoConnector, Settings):
        super().__init__(MongoConnector, Settings)

    def collection_name(self) -> str:
        return 'people'

    def create_new_person(self):
        person = {}
        await self.save_data()