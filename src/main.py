import logging

from fastapi import FastAPI

app = FastAPI()


@app.get("/home")
async def index():
    return {"message": "Hello world!"}
