import logging
from typing import Optional

from youtube_transcript_api import YouTubeTranscriptApi

from src.youtube.constants import LanguageCode
from src.youtube.exceptions import (
    InvalidLanguageCodeException,
    InvalidYouTubeURLException,
    TranscriptRetrievalException,
)
from src.youtube.utils import extract_video_id, is_valid_youtube_url, transcript_to_text

logger = logging.getLogger(__name__)


def get_transcript(video_url: str, lang: Optional[str]):
    if not is_valid_youtube_url(video_url):
        raise InvalidYouTubeURLException()

    if lang and lang not in {lang.value for lang in LanguageCode}:
        raise InvalidLanguageCodeException()

    try:
        transcript = get_transcript_ytt_api(video_url, lang)
        return transcript
    except Exception as e:
        logger.error(e)
        raise TranscriptRetrievalException() from e


def get_transcript_ytt_api(video_url: str, lang: Optional[str]):
    video_id = extract_video_id(video_url)

    if video_id is None:
        raise InvalidYouTubeURLException()

    ytt_api = YouTubeTranscriptApi()

    try:
        transcript_list = ytt_api.list(video_id)
    except Exception as e:
        logger.error(e)
        return None

    for transcript in transcript_list:
        default_transcript = transcript
        break

    if not default_transcript:
        return None

    if not lang:
        transcript = default_transcript.fetch()
        return transcript_to_text(transcript, is_translated=False)

    try:
        lang_transcript = transcript_list.find_transcript([lang])
    except Exception as e:
        logger.error(e)
        lang_transcript = None

    if lang_transcript:
        transcript = lang_transcript.fetch()
        is_translated = False
    else:
        transcript = default_transcript.translate(lang).fetch()
        is_translated = True

    return transcript_to_text(transcript, is_translated)
