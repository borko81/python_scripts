# Video download with factory pattern

from abc import ABC, abstractmethod
from enum import Enum, auto



class Quality(Enum):
    HIGH = auto()
    LOW = auto()


class BaseQuality(ABC):

    def prepare(self, folder):
        return folder

    @abstractmethod
    def convert(self):
        pass


class HighQuality(BaseQuality):
    def prepare(self, folder):
        return folder

    def convert(self):
        p = input("Show Path :")
        path = self.prepare(p)
        return f"Convert in high quality {path}"


class LowQuality(BaseQuality):
    def prepare(self, folder):
        return folder

    def convert(self):
        p = input("Show Path :")
        path = self.prepare(p)
        return f"Convert in low quality {path}"


def ask_user_for_quality() -> BaseQuality:
    download_factory = {
        Quality.HIGH.name: HighQuality(),
        Quality.LOW.name: LowQuality()
    }
    choice = input(f"Enter what quality do you want {list(q.name for q in Quality)} : ")
    try:
        return download_factory[choice]
    except KeyError:
        raise ValueError("Must enter one of choices")


if __name__ == '__main__':
    quality = ask_user_for_quality()
    print(quality.convert())
