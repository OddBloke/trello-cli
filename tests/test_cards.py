from click.testing import CliRunner

from trello_cli import main
from tests import utils


def test_cards_list_includes_all_returned_card_names(tmpdir, mocker):
    trello_client_mock = mocker.patch('trello_cli.get_authd_trello_from_file')

    board_names = ['eggs', 'spam', 'ham']
    board_mocks = utils.add_boards_to_mock(
        mocker, trello_client_mock, board_names)

    interesting_board_index = 1
    list_names = ['foo', 'bar', 'baz']
    board_mock = board_mocks[1]
    list_mocks = utils.add_lists_to_board_mock(mocker, board_mock, list_names)

    interesting_list_index = 1
    card_names = ['precise', 'trusty', 'xenial']
    list_mock = list_mocks[interesting_list_index]
    card_mocks = []
    for name in card_names:
        card_mock = mocker.Mock()
        card_mock.name = name
        card_mocks.append(card_mock)
    list_mock.list_cards.return_value = card_mocks

    runner = CliRunner()
    result = runner.invoke(
        main,
        ['cards', 'list', board_names[interesting_board_index],
         list_names[interesting_list_index]],
        catch_exceptions=False)
    assert result.exit_code == 0
    for name in card_names:
        assert name in result.output
