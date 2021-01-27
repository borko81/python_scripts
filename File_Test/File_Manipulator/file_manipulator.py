import os


def check_file_exists(filename):
    return os.path.exists(filename)


def create_file(filename):
    file = open(filename, 'w')
    file.close()


def add_content(filename, content):
    file = open(filename, 'a')
    file.write(content + '\n')
    file.close()


def replace_content(filename, old_str, new_str):
    if not check_file_exists(filename):
        print("An error occurred")
        return

    result = ''
    with open(filename, 'r') as input_file:
        for line in input_file.readlines():
            line = line.replace(old_str, new_str)
            result += line

    with open(filename, 'w') as output_file:
        print(result, file=output_file)


def delete_file(filename):
    if not check_file_exists(filename):
        print("An error occurred")
    else:
        os.remove(filename)


def read_command():
    while True:
        command = input()
        if command == 'End':
            break
        command = command.split('-')

        if command[0] == 'Create':
            create_file(command[1])

        elif command[0] == 'Add':
            filename = command[1]
            content = command[2]
            add_content(filename, content)

        elif command[0] == 'Replace':
            filename, old_str, new_str = command[1:]
            replace_content(filename, old_str, new_str)
        else:
            filename = command[1]
            delete_file(filename)


if __name__ == '__main__':
    read_command()
