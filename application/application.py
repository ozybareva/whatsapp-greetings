import asyncio
import logging
import uvicorn

from injector import Injector
from fastapi import FastAPI

from application.routers import PersonRouter
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from logic.data_loader import DataLoader
from logic.congratulator import Congratulator
from settings import Settings


class App:

    def __init__(self, container):
        self.container = Injector(container)
        self.app = FastAPI()
        self.loop = asyncio.get_event_loop()
        self.server = self.init_server(self.loop)
        self.settings = self.container.get(Settings)
        self.person_router = self.container.get(PersonRouter)
        self.congratulator = self.container.get(Congratulator)
        self.data_loader = self.container.get(DataLoader)
        self._scheduler = AsyncIOScheduler({'event_loop': self.loop})

    def start(self):
        self.add_routes()
        self._scheduler.start()

        try:
            logging.info(f'Start application')
            tasks = asyncio.gather(
                self.data_loader.load_contact_data_to_db(),
                self.server.serve()
            )
            self.loop.run_until_complete(tasks)

            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            logging.error(f'Unexpected error: {ex}')
        finally:
            self.loop.close()

    def init_server(self, loop):
        config = uvicorn.Config(app=self.app,
                                loop=loop,
                                host='0.0.0.0')

        return uvicorn.Server(config)

    def add_routes(self):
        self.app.add_api_route(
            '/load_new_person',
            self.person_router.load_new_person,
            methods=['POST']
        )

    def add_jobs(self):
        self._scheduler.add_job(
            self.congratulator.congratulate(),
            trigger='cron',
            second=self.settings.load_schedule_second,
            minute=self.settings.load_schedule_minute,
            hour=self.settings.load_schedule_hour,
            timezone='Asia/Tomsk'
        )

