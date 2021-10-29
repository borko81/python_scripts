from typing import Dict, Generator

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


def fib2(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, next + last
        yield next


for i in fib2(5):
    print(i)
