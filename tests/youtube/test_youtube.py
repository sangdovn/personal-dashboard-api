from src.youtube.constants import ErrorMessages
from tests.utils import client


def test_get_transcript_valid_url():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    lang = "en"
    response = client.get(f"/youtube/transcript?video_url={video_url}&lang={lang}")
    assert response.status_code == 200
    assert response.json().get("transcript") is not None
    assert isinstance(response.json().get("transcript"), str)


def test_get_transcript_invalid_url():
    response = client.get("/youtube/transcript?video_url=invalid_url&lang=en")
    assert response.status_code == 400
    assert response.json().get("detail") == ErrorMessages.INVALID_YOUTUBE_URL


def test_get_transcript_invalid_language_code():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    response = client.get(
        f"/youtube/transcript?video_url={video_url}&lang=invalid_lang"
    )
    assert response.status_code == 400
    assert response.json().get("detail") == ErrorMessages.INVALID_LANGUAGE_CODE
