class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temporary_node = self.head
        while temporary_node is not None:
            print(temporary_node.value)
            temporary_node = temporary_node.next


value = input("Enter the head for the new linked list: ")
my_linked_list = LinkedList(value)


printing = input("Do you want to print the linked list? (yes/no): ")
if printing.lower() == "yes":
    my_linked_list.print_list()
else:
    print("You chose not to print the linked list.")