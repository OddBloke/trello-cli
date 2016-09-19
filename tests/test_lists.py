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
    board_mock.all_lists.return_value = [
        mocker.Mock(name=name) for name in list_names]

    runner = CliRunner()
    result = runner.invoke(
        main, ['lists', 'list', board_names[interesting_board_index]],
        catch_exceptions=False)
    assert result.exit_code == 0
    for name in list_names:
        assert name in result.output
