import os.path

import click

from .auth import get_authd_trello_from_file


@click.command()
def main():
    client = get_authd_trello_from_file(os.path.expanduser('~/.trello.ini'))
    if client is None:
        raise click.ClickException('Configuration file does not exist.')
    for board in client.list_boards():
        print("* {}".format(board.name))
