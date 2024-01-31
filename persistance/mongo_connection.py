from motor.motor_asyncio import AsyncIOMotorClient
from settings import Settings


class MongoConnector:
    def __init__(self, settings: Settings):
        self._mongo_db = settings.db_mongo_name
        self._connection: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_dsn)

    def connect(self):
        db = self._connection.get_database(self._mongo_db)
        await db.list_collection_names()

    def get_connection(self):
        return self._connection
