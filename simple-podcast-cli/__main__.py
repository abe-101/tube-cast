import sys
import click
from index_script import convert_podcast
from my_scrapetube import return_channel, return_playlist

@click.group()
def cli():
    pass

@cli.command()
@click.argument('ids', nargs=-1)
def youtube_id(ids):
    click.echo(f'Converting Youtube Video to Anchor FM')
    ids = list(ids)
    click.echo(ids)

@cli.command()
@click.argument('filename', type=click.Path(exists=True))
def youtube_id_from_file(filename):
    click.echo(f'Converting Youtube Video (from file) to Anchor FM')
    ids = []
    with open(filename) as file:
        for row in file:
            ids.append(row.rstrip("\n"))
    print(ids)

@cli.command()
def youtube_channel():
    click.echo('Converting YouTube Channel to Anchor FM')

@cli.command()
def youtube_playlist():
    click.echo('Converting YouTube Playlist to Anchor FM')

if __name__ == '__main__':
    cli()
