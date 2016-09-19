from click.testing import CliRunner

from trello_cli import main
from tests import utils


def test_boards_list_includes_all_returned_board_names(tmpdir, mocker):
    trello_client_mock = mocker.patch('trello_cli.get_authd_trello_from_file')

    board_names = ['eggs', 'spam', 'ham']
    utils.add_boards_to_mock(mocker, trello_client_mock, board_names)

    runner = CliRunner()
    result = runner.invoke(main, ['boards', 'list'])
    assert result.exit_code == 0
    for name in board_names:
        assert name in result.output
