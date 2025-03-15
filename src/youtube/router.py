from fastapi import APIRouter, status

router = APIRouter(prefix="/youtube", tags=["YouTube"])

@router.get("/", status_code=status.HTTP_200_OK)
async def hello_youtube():
    return { "message": "Hello YouTube" }