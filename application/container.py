from injector import provider, singleton, Module

from application.routers import PersonRouter
from clients.whatsapp_client import WhatsAppClient
from persistance.mongo_connection import MongoConnector
from persistance.people_repository import PeopleRepository
from settings import Settings


class Container(Module):

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return Settings()

    @provider
    @singleton
    def provide_mongo_connection(self, settings: Settings) -> MongoConnector:
        return MongoConnector(settings)

    @provider
    @singleton
    def provide_people_repository(self, mongo: MongoConnector, settings: Settings) -> PeopleRepository:
        return PeopleRepository(mongo, settings)

    @provider
    @singleton
    def provide_wa_client(self, settings: Settings) -> WhatsAppClient:
        return WhatsAppClient(settings)

    @provider
    @singleton
    def provide_person_router(
            self,
            repository: PeopleRepository
    ) -> PersonRouter:
        return PersonRouter(repository)
