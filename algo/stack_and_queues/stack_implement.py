'''
LIFO, operation can be done O(1)
'''


class Stack:

    def __init__(self):
        self.stack = []

    # insert item into stack O(1)
    def push(self, data):
        self.stack.append(data)

    # implement pop method O(1)
    def pop(self):
        if not self.is_empty:
            data = self.stack[-1]
            del self.stack[-1]
            return data
        return "Stack is empty"

    def peek(self):
        try:
            return self.stack[-1]
        except IndexError as e:
            return e

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    test = Stack()
    # test.push(1)
    # test.push(2)
    # test.push(3)
    # print(test.stack_size())
    # print(test.is_empty())
    print(test.stack_size())
