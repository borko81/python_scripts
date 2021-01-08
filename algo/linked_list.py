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


if __name__ == '__main__':
    test = LinkedList()
    test.insert_start(1)

