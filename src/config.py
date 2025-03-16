from logging.config import dictConfig

from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from src.constants import LOGGING_CONFIG


def setup_logging():
    dictConfig(LOGGING_CONFIG)


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    model_config = ConfigDict(env_file=f".env")


settings = Settings()
