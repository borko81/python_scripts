from collections import deque

p = (1, 2)
x, y = p
print(x, y)


def drop_list(goods):
    first, middle, *last = goods
    return f"First is {first} middle is {middle} and finally: {', '.join(last)}"


print(drop_list(["name", "surname", "last name", "email"]))


def search(lines, pattern, history=5):
    prev_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)


FILE = r"anycode/text_for_work.txt"
with open(FILE, "r") as f:
    for line, prev in search(f, "Unbroken", 5):
        print(line)
        print("*" * 20)
        for p in prev:
            print(p.strip())
