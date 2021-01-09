class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        else:
            if node.rightChild:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)


test = BinarySearchTree()
test.insert(10)
test.insert(5)
test.insert(65)