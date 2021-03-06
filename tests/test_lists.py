from click.testing import CliRunner

from trello_cli import main
from tests import utils


def test_lists_list_includes_all_returned_list_names(tmpdir, mocker):
    trello_client_mock = mocker.patch('trello_cli.get_authd_trello_from_file')

    board_names = ['eggs', 'spam', 'ham']
    board_mocks = utils.add_boards_to_mock(
        mocker, trello_client_mock, board_names)

    interesting_board_index = 1
    list_names = ['foo', 'bar', 'baz']
    board_mock = board_mocks[interesting_board_index]
    utils.add_lists_to_board_mock(mocker, board_mock, list_names)

    runner = CliRunner()
    result = runner.invoke(
        main, ['lists', 'list', board_names[interesting_board_index]],
        catch_exceptions=False)
    assert result.exit_code == 0
    for name in list_names:
        assert name in result.output


def test_nice_error_given_for_missing_board(tmpdir, mocker):
    trello_client_mock = mocker.patch('trello_cli.get_authd_trello_from_file')

    board_names = ['eggs', 'spam', 'ham']
    utils.add_boards_to_mock(mocker, trello_client_mock, board_names)

    runner = CliRunner()
    result = runner.invoke(main, ['lists', 'list', "nonexistent"])
    assert result.exit_code > 0
    assert 'Traceback' not in result.output
