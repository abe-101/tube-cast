# Tube-Cast

![Cover image](https://github.com/abe-101/tube-cast/blob/2aecc4ec4565fe0ca90ca15d7fd136f004eb1534/assets/logo.jpg "Cover image")

A command-line tool that converts YouTube videos into Anchor FM podcasts.


## Installation


```
pip install tube-cast
```

## Usage
```bash
[user@ubuntu]$ tube-cast]$ tube-cast --help
Usage: tube-cast [OPTIONS] COMMAND [ARGS]...

  Convert YouTube video(s) to Anchor FM

Options:
  -d, --draft-mode      Save podcast as draft
  -t, --thumbnail_mode  Include YouTube thumbnail in podcast
  -u, --add-url         Add the YouTube URL To podcast description
  -x, --is-explicit     Mark podcast as explicit
  -h, --headless-mode
  --help                Show this message and exit.

Commands:
  youtube-channel       Takes in a YouTube Channel ID
  youtube-id            Takes in YouTube IDS as arguments
  youtube-id-from-file  Takes in a file containing youtube id (one per line)
  youtube-playlist      Takes in a YouTube Playlist ID
```

## Environment Variables

tube-cast will prompt the user for their email and password to anchor.fm
```bash
[user@ubuntu]$ tube-cast youtube-id
Enter anchor.FM user email: 
Enter anchor.FM password: 
```

The prompt can be avoided by exporting them as environment variables:
```bash
export ANCHOR_EMAIL='YOUR ANCHOR FM EMAIL HERE'
export ANCHOR_PASSWORD='YOUR ANCHOR FM PASSWORD HERE'
```

## Roadmap

* add better test case
* add better error catching
* include podcast publish date
* create documentation  
* Test tool in microsoft powershell
* ~~make available on pypi~~

## Authors

* [Abe](https:github.com/abe-101)

## Demo
[Click here](https://youtu.be/HBk-0wRGqHY "Tube-Cast Video Demo - YouTube") to view a video demo on YouTube, or watch below:


https://user-images.githubusercontent.com/82916197/176830848-dc5e7068-13ff-4d13-a9d7-055258692628.mp4


## Contributing

1. Fork it
2. Create your feature branch `git checkout -b my-new-feature`
3. Commit your changes `git commit -am 'Add some feature'`
4. Push to the branch `git push origin my-new-feature`
5. Create new Pull Request

## Known Issues

If you discover any bugs, feel free to create an issue on GitHub or create a fork and
send a pull request.

