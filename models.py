from enum import Enum, unique


@unique
class Where(Enum):
    zimuku = 'zimuku'
    shooter = 'shooter'


class Movie:
    def __init__(self) -> None:
        self.name = ''
        self.avatar_url = ''
        self.zimus = list()


class Zimu:
    def __init__(self) -> None:
        self.name = ''
        self.avatar_url = ''
        self.download_url = ''


class PageMovie:
    def __init__(self) -> None:
        self.movies = list()
        self.index = 0
        self.haveNext = False
