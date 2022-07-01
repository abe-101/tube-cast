# Tube-Cast
Streamline the conversion of your YouTube videos to Anchor FM (podcast)

tube-cast is a command-line tool that is capable of converting a youtube video into a podcast

[Click here](https://youtu.be/HBk-0wRGqHY "Tube-Cast Video Demo - YouTube") to view a full-length video demo on YouTube, or watch a quick version below:

## Instalation
```
pip install tube-cast
```

## Usage
```bash
Usage: tube-cast [OPTIONS] COMMAND [ARGS]...

  Convert YouTube video(s) to Anchor FM

Options:
  -d, --draft-mode      Save podcast as draft
  -t, --thumbnail_mode  Include YouTube thumbnail in podcast
  -u, --add-url         Add the YouTube URL To podcast description
  -x, --is-explicit     Mark podcast as explicit
  --help                Show this message and exit.

Commands:
  youtube-channel       Takes in a YouTube Channel ID
  youtube-id            Takes in YouTube IDS as arguments Where IDS is...
  youtube-id-from-file  Takes in a file containing youtube id (one per line)
  youtube-playlist      Takes in a YouTube Playlist ID
```
## Environment Variables
tube-cast will promt the user for their email and password to anchor.fm
```bash
[user@ubuntu]$ tube-cast youtube-id
Enter anchor.FM user email: 
Enter anchor.FM password: 
```

Users can avoid the promt by exporting them as environment variables:
```bash
export ANCHOR_EMAIL=
export ANCHOR_PASSWORD=
```
