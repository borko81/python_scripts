from collections import deque

data = "one two1 three four five six1 sever eight nine ten".split()


def search(mydata, pattern_to_search, history_len):
    prev_data = deque(maxlen=history_len)
    for line in mydata:
        if pattern_to_search in line:
            yield line, prev_data
        prev_data.append(line)


if __name__ == '__main__':
    for item, prev in search(data, '1', 3):
        print(item, list(prev))
