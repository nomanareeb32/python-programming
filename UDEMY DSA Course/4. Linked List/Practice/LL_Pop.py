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
        return True

    def pop(self):
        if self.length == 0:
            return None
        temporary_node = self.head
        previous_node = self.head
        while temporary_node.next is not None:
            previous_node = temporary_node
            temporary_node = temporary_node.next
        self.tail = previous_node
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temporary_node.value


value = input("Enter the head for the new linked list: ")
my_linked_list = LinkedList(value)


while True:
    action = input("\nWhat would you like to do? (print/append/pop/quit): ").lower()
    
    if action == "quit":
        print("Exiting program.")
        break
    
    elif action == "print":
        my_linked_list.print_list()
    
    elif action == "append":
        new_value = input("Enter the value to append: ")
        my_linked_list.append(new_value)
        print(f"Appended {new_value} to the linked list.")
    
    elif action == "pop":
        popped_value = my_linked_list.pop()
        if popped_value is None:
            print("The linked list is empty. Nothing to pop.")
        else:
            print(f"Popped {popped_value} from the linked list.")
    
    else:
        print("Invalid action. Please choose print, append, pop, or quit.")
