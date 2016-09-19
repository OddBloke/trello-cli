import uuid
from tempfile import TemporaryDirectory

from trello_cli import auth


def test_contents_of_ini_file_passed_to_client(tmpdir, mocker):
    # Set up a fake .trello.ini
    api_key, token = str(uuid.uuid4()), str(uuid.uuid4())
    creds = tmpdir.join(".trello.ini")
    creds.write("\n".join([
        "[auth]",
        "api_key = {}".format(api_key),
        "token = {}".format(token)]))

    mocked_client = mocker.patch('trello_cli.auth.TrelloClient')
    client = auth.get_authd_trello_from_file(str(creds))

    assert client == mocked_client.return_value
    assert [mocker.call(api_key=api_key, token=token)] == mocked_client.call_args_list


def test_none_returned_if_file_doesnt_exist(tmpdir):
    client = auth.get_authd_trello_from_file(str(tmpdir.join('non-existent')))
    assert client is None
