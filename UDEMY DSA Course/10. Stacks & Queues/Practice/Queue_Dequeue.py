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

    def dequeue(self):
        if self.length == 0:
            return print("Queue is empty. Cannot dequeue.")
        temporary_node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.length -= 1
        return temporary_node, temporary_node.value

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

    elif action == 'dequeue':
        dequeued_node, dequeued_value = queue.dequeue()
        if dequeued_node:
            print(f"Dequeued value: {dequeued_value}. Queue length is now: {queue.length}")
        
        action = input("Do you want to enqueue another value? (yes/no): ").strip().lower()