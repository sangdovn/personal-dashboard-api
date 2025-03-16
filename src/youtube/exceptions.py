from fastapi import status
from fastapi.exceptions import HTTPException


class InvalidYouTubeURLException(HTTPException):
    """Custom exception for invalid YouTube URLs."""

    def __init__(self, message: str = "The provided YouTube URL is invalid."):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class InvalidLanguageCodeException(HTTPException):
    """Custom exception for invalid language codes from client."""

    def __init__(self, message: str = "Invalid language code provided"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)


class TranscriptRetrievalException(HTTPException):
    """Custom exception for errors during transcript retrieval."""

    def __init__(self, message: str = "Failed to retrieve transcript"):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message
        )
