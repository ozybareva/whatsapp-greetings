from os import getenv, path
from pathlib import Path
from pydantic_settings import BaseSettings

base_dir = Path(__file__).parent.absolute()


class Settings(BaseSettings):
    wa_host: str = 'https://api.green-api.com'
    wa_media_host: str = 'https://media.green-api.com'
    wa_id_instance: str
    wa_api_token_instance: str

    mongo_host: str = 'mongo'
    mongo_port: int = 27017
    mongo_user: str = ''
    mongo_pass: str = ''
    mongo_db: str = ''

    @property
    def mongo_dsn(self) -> str:
        mongo_dsn = 'mongodb://{}:{}/{}'.format(
            self.db_mongo_host,
            self.db_mongo_port,
            self.db_mongo_auth,
        )
        return mongo_dsn

    class Config:
        config_file_name = f'{base_dir}/.env'
        if path.isfile(config_file_name):
            env_file = config_file_name
