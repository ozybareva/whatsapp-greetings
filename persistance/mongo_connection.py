from motor.motor_asyncio import AsyncIOMotorClient
from settings import Settings


class MongoConnector:
    def __init__(self, settings: Settings):
        self._mongo_db = settings.mongo_db
        self._connection: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_dsn)

    def get_connection(self):
        return self._connection
