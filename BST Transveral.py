class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        else:
            current = self.root
            while True:
                if value == current.value:
                    return None
                if value < current.value:
                    if current.left is None:
                        current.left = newNode
                        return self
                    current = current.left
                else:
                    if current.right is None:
                        current.right = newNode
                        return self
                    current = current.right

    def in_order(self, value):
        data = []

        def traverse(node):
            data.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        print(data)
        return 1 + data.index(value)


tree = BinarySearchTree()
# tree.insert(12)
# tree.insert(9)
# tree.insert(14)
# tree.insert(7)
# tree.insert(1)
# tree.insert(2)
# tree.insert(0)

# print(tree.in_order(9))
