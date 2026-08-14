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
        if temporary_node is None:
            print("The linked list is empty.")
            return
        while temporary_node is not None:
            print(temporary_node.value)
            temporary_node = temporary_node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

value = input("Enter the head for the new linked list: ")
my_linked_list = LinkedList(value)


printing = input("Do you want to print the linked list? (yes/no): ")
if printing.lower() == "yes":
    my_linked_list.print_list()
else:
    print("You chose not to print the linked list.")


appending = input("Do you want to append a new value to the linked list? (yes/no): ")
if appending.lower() == "yes":
    new_value = input("Enter the value to append: ")
    my_linked_list.append(new_value)
    print(f"Appended {new_value} to the linked list.")
