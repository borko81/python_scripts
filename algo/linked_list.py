'''Try to implement linked list'''


class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.numOfNodes = 0

    def insert_start(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # linear running time O(N)
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_list(self):
        '''Return size of list'''
        return self.numOfNodes

    def traverse(self):
        '''Jump to list, show item'''
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode

    def remove(self, data):
        assert self.head is not None

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode


if __name__ == '__main__':
    test = LinkedList()
    # test.insert_start(1)
    # test.insert_start(5)
    # test.insert_start(2)
    # print(test.size_of_list)
    # test.traverse()
    print(test.remove(1))
