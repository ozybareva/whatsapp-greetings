from settings import Settings
from persistance.mongo_connection import MongoConnector


class Repository:

    def __init__(
        self,
        mongodb_connection_manager: MongoConnector,
        settings: Settings,
    ) -> None:
        self.mongodb_connection_manager = mongodb_connection_manager
        self.database = settings.mongo_db

    @property
    def collection_name(self) -> str:
        raise NotImplementedError

    async def get_data(self, criteria: dict) -> dict | None:
        connection = await self.mongodb_connection_manager.get_connection()
        collection = connection[self.database][self.collection_name]
        return await collection.find_one(criteria)

    async def save_data(self, data: dict) -> str:
        connection = await self.mongodb_connection_manager.get_connection()
        result = await connection[self.database][self.collection_name].insert_one(data)
        return result.inserted_id
