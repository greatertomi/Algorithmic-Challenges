# Question Link
# https://www.codechef.com/problems/BSTOPS

class Node:
    def __init__(self, data, pos=1):
        self.key = data
        self.pos = pos
        self.right = None
        self.left = None


def insert(root, key, pos):
    if root is None:
        root = Node(key, pos)
        print(pos)
    elif key < root.key:
        root.left = insert(root.left, key, pos=(2 * pos))
    else:
        root.right = insert(root.right, key, pos=(2 * pos + 1))
    return root


def successor(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key, pr=True):
    if root is None:
        return
    elif key < root.key:
        root.left = deleteNode(root.left, key, pr)
    elif key > root.key:
        root.right = deleteNode(root.right, key, pr)
    else:
        if pr:
            print(root.pos)
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            temp = successor(root.right)
            root.key = temp.key
            root.right = deleteNode(root.right, temp.key, pr=False)
    return root


test = int(input())
root = None
while test > 0:
    op, x = input().split()
    x = int(x)
    if op == 'i':
        root = insert(root, x, 1)
    else:
        root = deleteNode(root, x)
    test -= 1
