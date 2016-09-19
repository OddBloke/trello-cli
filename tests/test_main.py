from click.testing import CliRunner

from trello_cli import main


def test_main_exits_nonzero_if_config_file_doesnt_exist(mocker):
    mocker.patch('trello_cli.get_authd_trello_from_file',
                 mocker.MagicMock(return_value=None))
    runner = CliRunner()
    result = runner.invoke(main, ['subcommand'])
    assert result.exit_code > 0
