import scrapetube


def return_channel(id: str):
    try:
        videos = scrapetube.get_channel(id)
        result = []
        for video in videos:
            result.append(video["videoId"])
        return result
    except:
        exit("Invalid channel id")


def return_playlist(id: str):
    try:
        videos = scrapetube.get_playlist(id)
        result = []
        for video in videos:
            result.append(video["videoId"])
        if len(result) == 0:
            raise Error
        return result
    except:
        exit("Invalid playlist id")
