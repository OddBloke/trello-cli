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


def _get_board(client, board_name):
    for board in client.list_boards():
        if board.name == board_name:
            return board
    raise click.ClickException('No board named "{}" found.'.format(board_name))


def _get_list(board, list_name):
    for l in board.all_lists():
        if l.name == list_name:
            return l
    raise click.ClickException('No list named "{}" found.'.format(list_name))


@main.group()
def lists():
    pass


@lists.command()  # NOQA
@click.argument('board-name')
@click.pass_context
def list(ctx, board_name):
    matching_board = _get_board(ctx.obj['client'], board_name)
    for l in matching_board.all_lists():
        print(l.name)


@main.group()
def cards():
    pass


@cards.command()  # NOQA
@click.argument('board-name')
@click.argument('list-name')
@click.pass_context
def list(ctx, board_name, list_name):
    matching_board = _get_board(ctx.obj['client'], board_name)
    matching_list = _get_list(matching_board, list_name)
    for card in matching_list.list_cards():
        print(card.name)
