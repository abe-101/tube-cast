import json
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

def download_youtube_thumbnail(youtube_id: str) -> str:
    URL = 'https://www.youtube.com/watch?v=' + youtube_id
    ydl_opts = {
            "outtmpl": "episode.%(ext)s",
            "skip_download": True,
            "no_warnings": True,
            "writethumbnail": True,
                }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)
    except Exception as e: 
        if isinstance(e, DownloadError):
            pass
        elif hasattr(e, 'message'):
            if "Command returned error code 23" in e.message:
                pass
            else:
                raise(e)
        else:
            raise(e)   
    return "episode.webp"

def download_youtube_video(youtube_id: str) -> dict:
    URL = 'https://www.youtube.com/watch?v=' + youtube_id
    ydl_opts = {
            #"outtmpl": "episode.mp3",
            "outtmpl": "episode.%(ext)s",
            "format": "bestaudio",
            "force-overwrites": True,
            "audio-format": 'mp3',
                }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URL)
            info = ydl.extract_info(URL)
    except Exception as e: 
        if isinstance(e, DownloadError):
            pass
        elif hasattr(e, 'message'):
            if "Command returned error code 23" in e.message:
                pass
            else:
                raise(e)
        else:
            raise(e)   
    return {'title': info['title'], 'description': info['description']}

'''
youtube_id = 'RPuhshpOv0o'
URL = 'https://www.youtube.com/watch?v=' + youtube_id
THUMBNAIL_FORMAT = "jpg"

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {
        #"outtmpl": "episode.mp3",
        "outtmpl": "episode.%(ext)s",
        "format": "bestaudio",
        "force-overwrites": True,
        "audio-format": 'mp3',
            }
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #info = ydl.extract_info(URL)
    ydl.download(URL)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
   # print(json.dumps(ydl.sanitize_info(info)))
'''
