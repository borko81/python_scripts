import string


def interact_read_file():
    while 1:
        try:
            reply = input("enter some number")
        except EOFError as e:
            print(e)
            break
        else:
            try:
                num = int(reply)
            except ValueError:
                break
            else:
                print(string.atoi(num))
    print("bye")


interact_read_file()
