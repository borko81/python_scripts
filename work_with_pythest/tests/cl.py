class Check:

    def __init__(self, number: int) -> None:
        self._number = number

    @property
    def number(self):
        return self._number

    def add_to_me(self, n):
        self._number += n


if __name__ == '__main__':
    c = Check(10)
    c.number = 100