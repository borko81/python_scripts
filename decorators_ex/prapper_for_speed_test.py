from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        print(f"Executing {fn.__name__} for {time() - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums(num):
    return sum(x for x in range(1, num + 1) if not x & 1)


@speed_test
def sum_nums_from_list(num):
    return sum([x for x in range(1, num + 1) if not x & 1])


print(sum_nums(1000000))
print(sum_nums_from_list(10000000))
