import configparser
import os.path

from trello import TrelloClient


def get_authd_trello_from_file(fn):
    if not os.path.exists(fn):
        return None
    config = configparser.ConfigParser()
    config.read(fn)
    return TrelloClient(api_key=config['auth']['api_key'],
                        token=config['auth']['token'])
