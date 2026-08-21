class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1


value = input("Enter the value for the head of the doubly linked list: ")
dll = DoublyLinkedList(value)

while True:
    action = input("\nWhat would you like to do? (append/pop/prepend/quit): ").lower()

    if action == "quit":
        print("Exiting program.")
        break

    elif action == "pop":
        popped_node = dll.pop()
        if popped_node:
            print(f"Popped | Node: {popped_node} | Value: {popped_node.value}")
        else:
            print("The doubly linked list is empty. Nothing to pop.")

    elif action == "append":
        new_value = input("Enter the value to append: ")
        dll.append(new_value)
        print(f"Appended | Node: {dll.tail} | Value: {dll.tail.value}")

    elif action == "prepend":
        new_value = input("Enter the value to prepend: ")
        dll.prepend(new_value)
        print(f"Prepended | Node: {dll.head} | Value: {dll.head.value}")

    else:
        print("Invalid action. Please choose append, pop, prepend, or quit.")