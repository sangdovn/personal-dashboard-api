import uvicorn
import os
from fastapi import FastAPI
from src.youtube.router import router as youtube_router
from src.config import settings

app = FastAPI()

# Register routers
app.include_router(youtube_router)


@app.get("/env")
def read_env():
    return {"env": os.getenv("ENV"), "database_url": settings.database_url}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
