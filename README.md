# Simple-Podcast
Streamline the conversion of your YouTube videos to Anchor FM (podcast)

## Environment Variables
There are two basic ways to set an environment variable from a bash or zsh terminal session. One is using the export keyword:
```bash
export ANCHOR_EMAIL=
export ANCHOR_PASSWORD=
export URL_IN_DESCRIPTION=true
export SAVE_AS_DRAFT=true
export LOAD_THUMBNAIL=true
```
Another way is to store them in a file called `load_env.env` and the program will export them.
```
cat <<< ' 
export ANCHOR_EMAIL=
export ANCHOR_PASSWORD=
export URL_IN_DESCRIPTION=true
export SAVE_AS_DRAFT=true
export LOAD_THUMBNAIL=true
' > simple-podcast-cli/load_env.env
```

## Dependencies
```bash
npm i youtube-dl puppeteer dotenv
```
