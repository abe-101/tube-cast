import scrapetube

def return_channel(id: str):
    videos = scrapetube.get_channel(id)
    result = []
    for video in videos:
        result.append(video['videoId'])
    return result


def return_playlist(id: str):
    videos = scrapetube.get_playlist(id)
    result = []
    for video in videos:
        result.append(video['videoId'])
    return result
