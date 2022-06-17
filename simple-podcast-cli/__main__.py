import sys
import click
from converter import convert_podcast
from my_scrapetube import return_channel, return_playlist

@click.group()
def cli():
    """Convert YouTube video(s) to Anchor FM"""
    pass

@cli.command()
@click.argument('ids', nargs=-1)
def youtube_id(ids):
    """Takes in YouTube ID(s) as arguments"""
    click.echo(f'Converting Youtube Video to Anchor FM')
    ids = list(ids)
    click.echo(ids)
    convert_podcast(ids)

@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def youtube_id_from_file(filename):
    """Takes in a file containing youtube id (one per line)"""
    click.echo(f'Converting Youtube Video (from file) to Anchor FM')
    ids = []
    with open(filename) as file:
        for row in file:
            ids.append(row.rstrip("\n"))
    print(ids)

@cli.command()
def youtube_channel():
    """Takes in a YouTube Channel ID"""
    click.echo('Converting YouTube Channel to Anchor FM')

@cli.command()
def youtube_playlist():
    """Take in a YouTube Playlist ID"""
    click.echo('Converting YouTube Playlist to Anchor FM')

if __name__ == '__main__':
    cli()
