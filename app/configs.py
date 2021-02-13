from pydantic import BaseSettings

class Configs(BaseSettings):
    # is in debug
    DEBUG_MODE: bool = True
    APP_NAME: str = 'InStock'

configs = Configs()
