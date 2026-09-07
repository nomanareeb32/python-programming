class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

try:
    value = int(input("Enter a value to initialize the queue: "))
    queue = Queue(value)
    print(f"Queue initialized with value: {queue.first.value}")
except ValueError:
    print("Invalid input. Please enter an integer only.")