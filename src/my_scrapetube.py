import scrapetube


def return_channel(id: str):
    try:
        videos = scrapetube.get_channel(id)
        return [video["videoId"] for video in videos]
    except:
        exit("Invalid channel id")


def return_playlist(id: str):
    try:
        videos = scrapetube.get_playlist(id)
        result = [video["videoId"] for video in videos]
        if len(result) == 0:
            raise Error
        return result
    except:
        exit("Invalid playlist id")
