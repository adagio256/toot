from collections import namedtuple
from dataclasses import dataclass

from aiohttp import ClientSession

__version__ = '0.36.0'

App = namedtuple('App', ['instance', 'base_url', 'client_id', 'client_secret'])
User = namedtuple('User', ['instance', 'username', 'access_token'])

DEFAULT_INSTANCE = 'https://mastodon.social'

CLIENT_NAME = 'toot - a Mastodon CLI client'
CLIENT_WEBSITE = 'https://github.com/ihabunek/toot'


@dataclass
class Context:
    app: App
    user: User
    session: ClientSession
