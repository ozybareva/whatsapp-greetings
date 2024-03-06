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

    async def get_data(self, criteria: dict) -> list | None:
        connection = self.mongodb_connection_manager.get_connection()
        cursor = connection[self.database][self.collection_name].find(criteria)
        result = []
        async for data in cursor:
            result.append(data)
        return result

    async def save_data(self, data: dict) -> str:
        connection = self.mongodb_connection_manager.get_connection()
        result = await connection[self.database][self.collection_name].insert_one(data)
        return result.inserted_id
