import uvicorn
from fastapi import FastAPI

from src.config import setup_logging
from src.youtube.router import router as youtube_router

setup_logging()

app = FastAPI()

# Register routers
app.include_router(youtube_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
