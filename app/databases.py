from typing import Optional
from pydantic import BaseSettings, Field

class MariaDbConnection(BaseSettings):
    username: str = Field(default='root', env='mariadb_username')
    password: str = Field(default='', env='mariadb_password')
    host: str = Field(default='localhost', env='mariadb_host')
    port: int = Field(default=3306, env='mariadb_port')
    database: str = Field(default='instock', env='mariadb_dbname')
    unix_socket: Optional[str]
    connect_timeout: Optional[int]
    read_timeout: Optional[int]
    write_timeout: Optional[int]
    compress: Optional[bool]

    class Config:
        env_file = '.env'
