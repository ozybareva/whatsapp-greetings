from os import path
from pathlib import Path
from pydantic_settings import BaseSettings

base_dir = Path(__file__).parent.parent.absolute()


class Settings(BaseSettings):
    wa_host: str = 'https://api.green-api.com'
    wa_media_host: str = 'https://media.green-api.com'
    wa_id_instance: str
    wa_api_token_instance: str

    mongo_host: str = 'localhost'
    mongo_port: int = 27017
    mongo_db: str = 'wa'

    load_schedule_second: str = '00'
    load_schedule_minute: str = '30'
    load_schedule_hour: str = '11'

    @property
    def mongo_dsn(self) -> str:
        mongo_dsn = 'mongodb://{}:{}/{}'.format(
            self.mongo_host,
            self.mongo_port,
            self.mongo_db
        )
        return mongo_dsn

    class Config:
        config_file_name = f'{base_dir}/.env'
        if path.isfile(config_file_name):
            env_file = config_file_name
