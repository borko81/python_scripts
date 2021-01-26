def convert_list_to_numbers(arr):
    return map(int, arr)


def calcuate_sum_from_file(file):
    result = [num.rstrip("\n") for num in file.readlines()]
    return sum(convert_list_to_numbers(result))


def check_for_file(file):
    try:
        f = open(file)
    except IOError as e:
        print(e)
    else:
        return calcuate_sum_from_file(f)


print(check_for_file("numbers.txt"))
