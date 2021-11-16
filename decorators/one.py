from functools import wraps
import logging

logging.basicConfig(filename='logfile.log',
                    filemode='a',
                    format=(
                        '%(asctime)s-%(name)s : %(message)s'
                    ),
                    level=logging.DEBUG
                    )


def my_decorator(func):
    def wrapper(*args, **kwargs):
        logging.debug("Choice name {}".format(*args))
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def say_hi(name):
    return name


def check_who_is_enter(names):
    def global_decodator(func):
        @wraps(func)
        def wrpapper(*args, **kwargs):
            if names == 'borko':
                return func(*args, **kwargs)
            else:
                return("User with name {} not allowed to run function {}".format(names, func.__name__))
        return wrpapper
    return global_decodator


@check_who_is_enter(say_hi("borko"))
def return_something():
    return "Allowed"


print(return_something())
