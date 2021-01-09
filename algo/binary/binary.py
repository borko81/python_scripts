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

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def get_max_value(self):
        if self.root is not None:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild is not None:
            return self.get_max(node.rightChild)

        return node.data

    def get_min_value(self):
        if self.root is not None:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild is not None:
            return self.get_min(node.leftChild)

        return node.data

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print(f"{node.data}")

        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)
        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print("Removing {}".format(node.data))
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rigthChild == node:
                    parent.rightChild = None

                if parent is None:
                    self.root = None

                del node

            elif node.leftChild is None and node.rigthChild is not None:
                print("Removing a node with single right child ")
                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self.root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rigthChild is None and node.leftChild is not None:
                print("removing a node with a single left child")
                parent = node.parent

                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                    else:
                        self.root = node.leftChild

                    node.leftChild.parent = parent
                    del node
            else:
                print("Removing with two child")



test = BinarySearchTree()
test.insert(10)
test.insert(5)
test.insert(65)
test.traverse()
print(test.get_max_value())
print(test.get_min_value())
