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
                    "format": "%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                }
            },
            "loggers": {
                "uvicorn": {"handlers": ["console"], "level": "INFO"},
                "app_logger": {"handlers": ["console"], "level": "INFO"},
            },
        }
    )


setup_logging()


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")


settings = Settings()
