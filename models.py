import json
from enum import Enum, unique


@unique
class Where(Enum):
    zimuku = 'zimuku'
    shooter = 'shooter'


class Base:
    @property
    def to_json(self):
        return self.__dict__

    def json(self):
        return json.dumps(self, default=lambda obj: obj.to_json, ensure_ascii=False)


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
    def __init__(self, movies=None, currentIndex=-1, haveNext=False) -> None:
        self.movies = movies
        self.currentIndex = currentIndex
        self.haveNext = haveNext


class Resp(Base):
    def __init__(self, obj=None, errorMsg='') -> None:
        self.success = True  # 标识解析是否出错了
        if errorMsg and errorMsg.strip():
            self.success = False

        self.errorMsg = errorMsg  # 记录出错的信息
        self.obj = obj
