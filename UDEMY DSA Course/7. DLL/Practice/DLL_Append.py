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


value = input("Enter the value for the head of the doubly linked list: ")
dll = DoublyLinkedList(value)

action = input("Do you want to append a new value to the doubly linked list? (yes/no): ")
if action.lower() == 'yes':
    new_value = input("Enter the value to append: ")
    dll.append(new_value)
    print(f"Appended {new_value} to the doubly linked list.")
else:
    print("No value appended to the doubly linked list.")