import os
import subprocess
import json


def convert_podcast(videos: list) -> dict:
    podcast_env = {
        "ANCHOR_EMAIL": os.getenv("ANCHOR_EMAIL"),
        "ANCHOR_PASSWORD": os.getenv("ANCHOR_PASSWORD"),
        "URL_IN_DESCRIPTION": os.getenv("URL_IN_DESCRIPTION", "false"),
        "SAVE_AS_DRAFT": os.getenv("SAVE_AS_DRAFT", "false"),
        "LOAD_THUMBNAIL": os.getenv("LOAD_THUMBNAIL", "false"),
    }

    result = dict()

    for video in videos:
        video_id_json = json.dumps({"id": video})
        with open("episode.json", "w") as file:
            file.write(video_id_json)
        try:
            p = subprocess.run(
                ["/usr/bin/node", "index.js"], check=True, env=podcast_env
            )

            print(video + " Completed")
            result[video] = "succeeded"
        except subprocess.CalledProcessError:
            print(video + " Failed")
            result[video] = "Failed"

    # Clean up downloaded files
    for file in "episode.json", "episode.mp3", "thumbnail.jpg":
        if os.path.isfile(file):
            os.remove(file)

    return result
