from typing import Optional

from fastapi import APIRouter, Query, status

from src.youtube.services import get_transcript

router = APIRouter(prefix="/youtube", tags=["YouTube"])


@router.get("/transcript", status_code=status.HTTP_200_OK)
async def read_transcript(
    video_url: str = Query(...),
    lang: Optional[str] = Query(None),
):
    transcript = get_transcript(video_url, lang)
    return (
        {"transcript": transcript}
        if transcript
        else {"transcript": "No transcript available"}
    )
