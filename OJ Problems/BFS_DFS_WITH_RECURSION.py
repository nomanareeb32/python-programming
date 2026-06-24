stream = [2, 3, 4, 5, "null", 6, 7]
visited = []


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


def dfs(node):
    if node is None:
        print(None)
        return
    print(node.value)
    dfs(node.left)
    dfs(node.right)


def bfs(node):
    global visited

    print(node.value)

    visited.pop(0)
    if node.left is not None:
        visited.append(node.left)

    if node.right is not None:
        visited.append(node.right)

    if len(visited) > 0:
        bfs(visited[0])


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
        if n.right is not None:
            arr.append(n.right)
        if n.left is not None:
            arr.append(n.left)
        if len(arr) <= 0:
            return False
        n = arr.pop(len(arr) - 1)


root = constructGraph()
# dfs(root)
visited.append(root)
bfs(root)
