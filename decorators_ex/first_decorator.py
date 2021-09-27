# F1

def add_more_message(fn):
    def wrapper():
        print('This is the top of the top')
        print(fn())
        print('This is the bottom')
    return wrapper


@add_more_message
def show_message():
    return 'Message one'


show_message()
