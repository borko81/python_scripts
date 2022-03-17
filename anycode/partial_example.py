from functools import partial


def multiply(a: int|float, b: int|float) -> int|float:
    return a * b


def double_me(a: int|float) -> int|float:
    return multiply(a, 2)


print(multiply(10, 2))
result = double_me(5)
print(result)


double = partial(multiply, b=2)
print("|".join([str(double(x)) for x in range(1, 11, 1)]))