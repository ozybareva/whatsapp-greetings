from motor.motor_asyncio import AsyncIOMotorClient
from settings import Settings


class MongoConnector:
    def __init__(self, settings: Settings):
        self._mongo_db = settings.mongo_db
        self._connection: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_dsn)

    async def connect(self):
        db = self._connection.get_database(self._mongo_db)
        await db.list_collection_names()

    def get_connection(self):
        return self._connection
