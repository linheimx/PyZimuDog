from enum import Enum, unique


@unique
class Where(Enum):
    zimuku = 'zimuku'
    shooter = 'shooter'


class Base:
    @property
    def to_json(self):
        return self.__dict__


class Movie(Base):
    def __init__(self) -> None:
        self.name = ''
        self.avatar_url = ''
        self.detail_url = ''


class Zimu(Base):
    def __init__(self) -> None:
        self.name = ''
        self.avatar_url = ''
        self.detail_url = ''
        self.download_url = ''


class PageMovie(Base):
    def __init__(self, movies, currentIndex, haveNext) -> None:
        self.movies = movies
        self.currentIndex = currentIndex
        self.haveNext = haveNext
