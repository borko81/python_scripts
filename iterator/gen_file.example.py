# Generate infinity number
# serach for primary number and add to array
# as much as you want

from typing import Generator, List


def gen_numbers() -> Generator[int, None, None]:
    i: int = 1
    while True:
        yield i
        i = i + 1


def check_is_prime() -> Generator[int, None, None]:
    for n in gen_numbers():
        ok = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                ok = False
                break
        if ok:
            yield n


def take(how_much, function) -> int:
    result: List[int] = []
    arr = iter(function)
    for n in range(how_much):
        result.append(next(arr))
    return result


if __name__ == '__main__':
    print(take(20, check_is_prime()))
