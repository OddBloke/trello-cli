def add_boards_to_mock(mocker, trello_client_mock, board_names):
    board_mocks = []
    for name in board_names:
        board_mock = mocker.Mock()
        board_mock.name = name
        board_mocks.append(board_mock)
    trello_client_mock.return_value.list_boards.return_value = board_mocks
    return board_mocks


def add_lists_to_board_mock(mocker, board_mock, list_names):
    list_mocks = []
    for name in list_names:
        list_mock = mocker.Mock()
        list_mock.name = name
        list_mocks.append(list_mock)
    board_mock.all_lists.return_value = list_mocks
    return list_mocks
