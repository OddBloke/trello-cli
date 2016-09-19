from click.testing import CliRunner

from trello_cli import main


def test_lists_list_includes_all_returned_list_names(tmpdir, mocker):
    trello_client_mock = mocker.patch('trello_cli.get_authd_trello_from_file')

    board_names = ['eggs', 'spam', 'ham']
    board_mocks = []
    for name in board_names:
        board_mock = mocker.Mock()
        board_mock.name = name
        board_mocks.append(board_mock)
    trello_client_mock.return_value.list_boards.return_value = board_mocks

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
