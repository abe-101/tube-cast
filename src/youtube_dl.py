import json
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError


def download_youtube_thumbnail(youtube_id: str) -> bool:
    URL = "https://www.youtube.com/watch?v=" + youtube_id
    ydl_opts = {
        "outtmpl": "episode.%(ext)s",
        "skip_download": True,
        "no_warnings": True,
        "writethumbnail": True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)
            return "episode.webp"
    except Exception as e:
        if isinstance(e, DownloadError):
            pass
        elif hasattr(e, "message"):
            if "Command returned error code 23" in e.message:
                pass
            else:
                raise (e)
        else:
            raise (e)
    return False


def download_youtube_video(youtube_id: str) -> dict:
    URL = "https://www.youtube.com/watch?v=" + youtube_id
    ydl_opts = {
        # "outtmpl": "episode.mp3",
        "outtmpl": "episode.%(ext)s",
        "format": "bestaudio",
        "force_overwrites": True,
        "audio_format": "mp3",
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)
            info = ydl.extract_info(URL)
        return {
            "title": info["title"],
            "description": info["description"],
            "file_name": "episode.webm",
        }
    except Exception as e:
        if isinstance(e, DownloadError):
            pass
        elif hasattr(e, "message"):
            if "Command returned error code 23" in e.message:
                pass
            else:
                raise (e)
        else:
            raise (e)
    return False
