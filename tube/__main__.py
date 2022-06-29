import sys
import os
import click
import getpass
from validate_id import valid_id
from my_scrapetube import return_channel, return_playlist
from youtube_to_anchorFM import convert_youtube_to_podcast

@click.group()
@click.option("-d", "--draft-mode", is_flag=True, help="Save podcast as draft")
@click.option('-t', '--thumbnail', is_flag=True, help="Include YouTube thumbnail in podcast")
@click.option('-u', '--add-url', is_flag=True, help="Add YouTube url to podcast description")
@click.option('-x', '--is-explicit', is_flag=True, help="Mark podcast as explicit")
@click.pass_context
def cli(ctx, draft_mode, thumbnail, add_url, is_explicit):
    """Convert YouTube video(s) to Anchor FM"""
    ctx.ensure_object(dict)

    ctx.obj['DRAFT_MODE'] = draft_mode
    ctx.obj['THUMBNAIL'] = thumbnail
    ctx.obj['ADD_URL'] = add_url
    ctx.obj['IS_EXPLICIT'] = is_explicit

    if not os.getenv("ANCHOR_EMAIL") or not os.getenv("ANCHOR_PASSWORD"):
        os.environ["ANCHOR_EMAIL"] = input("Enter anchor.FM user email: ")
        os.environ["ANCHOR_PASSWORD"] = getpass.getpass("Enter anchor.FM password: ")
    pass

@cli.command()
@click.pass_context
@click.argument('ids', nargs=-1)
def youtube_id(ctx, ids):
    """Takes in YouTube ID(s) as arguments"""
    click.echo(f'Converting Youtube Video to Anchor FM')
    click.echo(f'draft_value: {ctx.obj}')

    ids = list(ids)
    click.echo(ids)
    for id in ids:
        if valid_id(id):
            convert_youtube_to_podcast(id, ctx.obj)
        else:
            print("Id: " + id + " is Invalid - Skipping")

@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def youtube_id_from_file(filename, draft_mode, thumbnail, add_url, is_explicit):
    """Takes in a file containing youtube id (one per line)"""
    click.echo(f'Converting Youtube Video (from file) to Anchor FM')
    ids = []
    with open(filename) as file:
        for row in file:
            ids.append(row.rstrip("\n"))
    print(ids)

@cli.command()
def youtube_channel(draft_mode, thumbnail, add_url, is_explicit):
    """Takes in a YouTube Channel ID"""
    click.echo('Converting YouTube Channel to Anchor FM')

@cli.command()
def youtube_playlist(draft_mode, thumbnail, add_url, is_explicit):
    """Take in a YouTube Playlist ID"""
    click.echo('Converting YouTube Playlist to Anchor FM')

if __name__ == '__main__':
    cli()
