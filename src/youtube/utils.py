import json
import re


def is_valid_youtube_url(url: str) -> bool:
    """Validate if the provided value is a valid YouTube URL or video ID."""

    video_id_pattern = r"^[a-zA-Z0-9_-]{11}$"
    url_pattern = r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)[a-zA-Z0-9_-]{11}"
    return bool(re.match(url_pattern, url) or re.match(video_id_pattern, url))


def extract_video_id(value: str) -> str:
    """Extract the video ID from a YouTube URL."""

    pattern = r"(?:https?://)?(?:www\.)?(?:youtube\.com/(?:[^/]+/.*/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, value)
    return match.group(1) if match else None


def json3_to_text(json3_str: str):
    try:
        data = json.loads(json3_str)
        if "events" not in data:
            return None

        texts = []
        for event in data["events"]:
            if "segs" not in event:
                continue

            for segment in event["segs"]:
                text = segment["utf8"]
                if text and text.strip():
                    texts.append(text.strip())

        return " ".join(texts)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON3 format") from e


def transcript_to_text(transcript, is_translated) -> str:
    transcript_type = None
    if transcript.is_generated and is_translated:
        transcript_type = "[translated from auto-generated]"
    elif transcript.is_generated:
        transcript_type = "[auto-generated]"
    elif is_translated:
        transcript_type = "[translated]"

    texts = []

    for snippet in transcript.snippets:
        stripped_text = snippet.text.strip()
        if stripped_text:
            texts.append(stripped_text)

    joined_text = " ".join(texts)
    if transcript_type:
        return f"{transcript_type} {joined_text}"
    return joined_text
