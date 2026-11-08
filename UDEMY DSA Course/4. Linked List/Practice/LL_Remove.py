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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temporary_node = self.head
        self.head = self.head.next
        temporary_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temporary_node.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temporary_node = self.head
        for _ in range(index):
            temporary_node = temporary_node.next
        return temporary_node.value

    def set(self, index, value):
        try:
            temporary_node = self.get(index)
            if temporary_node is not None:
                temporary_node.value = value
                return True
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temporary_node = self.get(index - 1)
        new_node.next = temporary_node.next
        temporary_node.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        previous_node = self.get(index - 1)
        temporary_node = previous_node.next
        previous_node.next = temporary_node.next
        temporary_node.next = None
        self.length -= 1
        return temporary_node.value
    

value = input("Enter the head for the new linked list: ")
my_linked_list = LinkedList(value)


while True:
    action = input("\nWhat would you like to do? (print/append/pop/pop_first/prepend/get/set/insert/remove/quit): ").lower()
    
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
    
    elif action == "pop_first":
        popped_value = my_linked_list.pop_first()
        if popped_value is None:
            print("The linked list is empty. Nothing to pop.")
        else:
            print(f"Popped {popped_value} from the linked list.")

    elif action == "get":
        try:
            index = int(input("Enter the index to get: "))
            value_at_index = my_linked_list.get(index)
            if value_at_index is None:
                print(f"No node found at index {index}.")
            else:
                print(f"Value at index {index}: {value_at_index}")
        except ValueError:
            print("Please enter a valid integer index.")

    elif action == "set":
        try:
            index = int(input("Enter the index to set: "))
            new_value = input("Enter the new value: ")
            success = my_linked_list.set(index, new_value)
            if success:
                print(f"Set value at index {index} to {new_value}.")
            else:
                print(f"Failed to set value at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "insert":
        try:
            index = int(input("Enter the index to insert at: "))
            new_value = input("Enter the new value to insert: ")
            success = my_linked_list.insert(index, new_value)
            if success:
                print(f"Inserted {new_value} at index {index}.")
            else:
                print(f"Failed to insert {new_value} at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "remove":
        try:
            index = int(input("Enter the index to remove: "))
            removed_value = my_linked_list.remove(index)
            if removed_value is not None:
                print(f"Removed value at index {index}: {removed_value}")
            else:
                print(f"Failed to remove value at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid action. Please choose print, append, pop, pop_first, get, insert, remove, or quit.")
