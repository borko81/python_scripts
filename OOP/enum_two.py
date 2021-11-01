from enum import Enum


class Status(Enum):
    success = 0
    error = 1
    warning = 2


print(f"Exit status is {Status.error}")
