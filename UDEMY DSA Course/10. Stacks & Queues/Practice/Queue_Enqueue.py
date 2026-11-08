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
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

try:
    value = int(input("Enter a value to initialize the queue: "))
    queue = Queue(value)
    print(f"Queue initialized with value: {queue.first.value}")
except ValueError:
    print("Invalid input. Please enter an integer only.")

while True:
    action = input("Do you want to enqueue a new value? (yes/no): ").strip().lower()
    if action == 'no':
        break

    elif action == 'yes':
        try:
            new_value = int(input("Enter a value to enqueue: "))
            queue.enqueue(new_value)
            print(f"Enqueued value: {new_value}. Queue length is now: {queue.length}")
        except ValueError:
            print("Invalid input. Please enter an integer only.")
        
        action = input("Do you want to enqueue another value? (yes/no): ").strip().lower()