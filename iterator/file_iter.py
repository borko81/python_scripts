class Foo:

    def __init__(self, collection) -> None:
        self.collection = collection
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.collection):
            raise StopIteration
        val = self.collection[self.counter]
        self.counter += 1
        return val


def generator():
    yield "a"
    yield "a"


def baz():
    yield from range(10)


def bar():
    yield from range(5)


def main():
    yield from bar()
    print('-' * 10)
    yield from baz()


for v in main():
    print(v)
