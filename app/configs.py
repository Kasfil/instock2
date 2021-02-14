from pydantic import BaseSettings, Field
from app.databases import MariaDbConnection

class Configs(BaseSettings):
    # is in debug
    DEBUG_MODE: bool = True
    APP_NAME: str = 'InStock'
    DEFAULT_DB: MariaDbConnection = MariaDbConnection()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

configs = Configs()
