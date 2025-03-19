from logging.config import dictConfig

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


def setup_logging():
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "DEBUG",
                }
            },
            "loggers": {
                "uvicorn": {
                    "handlers": ["console"],
                    "level": "DEBUG",
                },
                "app_logger": {
                    "handlers": ["console"],
                    "level": "DEBUG",
                },
            },
        }
    )


setup_logging()


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")


settings = Settings()
