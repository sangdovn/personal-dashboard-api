import logging

from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/home")
async def index():
    logger.info("Hello world!")
    return {"message": "Hello world!"}
