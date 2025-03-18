from fastapi import status
from fastapi.exceptions import HTTPException

from src.youtube.constants import ErrorMessages


class InvalidYouTubeURLException(HTTPException):
    """Custom exception for invalid YouTube URLs."""

    def __init__(self, message: str = ErrorMessages.INVALID_YOUTUBE_URL):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class InvalidLanguageCodeException(HTTPException):
    """Custom exception for invalid language codes from client."""

    def __init__(self, message: str = ErrorMessages.INVALID_LANGUAGE_CODE):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class TranscriptRetrievalException(HTTPException):
    """Custom exception for errors during transcript retrieval."""

    def __init__(self, message: str = ErrorMessages.TRANSCRIPT_RETRIEVAL_FAILURE):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
        )
