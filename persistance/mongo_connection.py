from motor.motor_asyncio import AsyncIOMotorClient
from settings import Settings


class MongoConnection:
    def __init__(self, settings: Settings):
        self._mongo_db = settings.db_mongo_name
        self._connection: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_dsn)

    async def get_data(self, criteria: dict) -> dict | None:
        collection = self._connection[self.database][self.collection_name]
        return await collection.find_one(criteria)

    async def save_data(self, data: dict) -> str:
        connection = await self.mongodb_connection_manager.get_connection()
        result = await connection[self.database][self.collection_name].insert_one(data)
        return result.inserted_id