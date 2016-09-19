import os.path

import click

from .auth import get_authd_trello_from_file


@click.group()
@click.pass_context
def main(ctx):
    client = get_authd_trello_from_file(os.path.expanduser('~/.trello.ini'))
    if client is None:
        raise click.ClickException('Configuration file does not exist.')
    ctx.obj = {'client': client}


@main.group()
def boards():
    pass


@boards.command()
@click.pass_context
def list(ctx):
    for board in ctx.obj['client'].list_boards():
        print(board.name)


@main.group()
def lists():
    pass


@lists.command()  # NOQA
@click.argument('board-name')
@click.pass_context
def list(ctx, board_name):
    matching_board = None
    for board in ctx.obj['client'].list_boards():
        if board.name == board_name:
            matching_board = board
            break
    for l in matching_board.all_lists():
        print(l.name)
