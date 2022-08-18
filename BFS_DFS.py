stream = [2, 3, 4, 5, "null", 6, 7]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def constructGraph():
    node_p = Node(2)
    node_p.left = Node(3)
    node_p.right = Node(4)
    node_p.left.left = Node(5)
    node_p.right.left = Node(6)
    node_p.right.right = Node(7)
    return node_p


def bfs(n, t):
    arr = []

    while True:
        print(n.value)
        if n.value == t:
            return True

        if n.left is not None:
            arr.append(n.left)

        if n.right is not None:
            arr.append(n.right)

        if len(arr) <= 0:
            return False

        n = arr.pop(0)


def dfs(n, t):
    arr = []

    while True:
        print(n.value)
        if n.value == t:
            return True

        if n.right != None:
            arr.append(n.right)

        if n.left != None:
            arr.append(n.left)

        if len(arr) <= 0:
            return False

        n = arr.pop(len(arr) - 1)


root = constructGraph()
print(bfs(root, 9))
print(dfs(root, 9))
