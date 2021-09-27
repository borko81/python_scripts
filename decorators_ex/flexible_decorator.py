from functools import wraps


def name_upper(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """ Wrapper doc"""
        print(fn.__name__)
        print(fn.__doc__)
        result = fn(*args, **kwargs)
        return result.upper()
    return wrapper


@name_upper
def show_name(name, surname):
    """ Show name doc """
    return f'Hello {name} {surname}'


result = show_name('first', 'last')
print(result)
print(show_name.__name__)
print(show_name.__doc__)
