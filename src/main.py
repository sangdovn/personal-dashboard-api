from fastapi import FastAPI

from src.config import setup_logging
from src.youtube.router import router as youtube_router

setup_logging()

app = FastAPI(
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redocs",
)

# Register routers
app.include_router(youtube_router)
