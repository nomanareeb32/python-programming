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
            print(f"Node: {temporary_node} | Value: {temporary_node.value}")
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
        return temporary_node

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
        return temporary_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temporary_node = self.head
        for _ in range(index):
            temporary_node = temporary_node.next
        return temporary_node  # returns the node object

    def set(self, index, value):
        try:
            temporary_node = self.get(index)
            if temporary_node is not None:
                temporary_node.value = value
                return temporary_node
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

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
        return new_node  # returns the newly inserted node

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
        return temporary_node  # returns the removed node

    def reverse(self):
        if self.length <= 1:
            return
        temporary_node = self.head
        self.head = self.tail
        self.tail = temporary_node
        after = temporary_node.next
        before = None
        for _ in range(self.length):
            after = temporary_node.next
            temporary_node.next = before
            before = temporary_node
            temporary_node = after

    def find_middle_node(self):
        if self.length == 0:
            return None
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

    def has_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

    def find_kth_node_from_end(self, k):
        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow

    def remove_duplicates(self):
        if self.length == 0:
            return "The linked list is empty. No duplicates to remove."
        curent_node = self.head
        runner_node = self.head
        while curent_node is not None:
            runner_node = curent_node
            while runner_node.next is not None:
                if runner_node.next.value == curent_node.value:
                    runner_node.next = runner_node.next.next
                    self.length -= 1
                else:
                    runner_node = runner_node.next
            curent_node = curent_node.next

value = input("Enter the head for the new linked list: ")
my_linked_list = LinkedList(value)


while True:
    action = input("\nWhat would you like to do? (print/append/pop/pop_first/prepend/get/set/insert/remove/reverse/findmiddle/hasloop/findkthfromend/remove_duplicates/quit): ").lower()

    if action == "quit":
        print("Exiting program.")
        break

    elif action == "print":
        my_linked_list.print_list()

    elif action == "append":
        new_value = input("Enter the value to append: ")
        my_linked_list.append(new_value)
        print(f"Appended | Node: {my_linked_list.tail} | Value: {my_linked_list.tail.value}")

    elif action == "prepend":
        new_value = input("Enter the value to prepend: ")
        my_linked_list.prepend(new_value)
        print(f"Prepended | Node: {my_linked_list.head} | Value: {my_linked_list.head.value}")

    elif action == "pop":
        popped_node = my_linked_list.pop()
        if popped_node is None:
            print("The linked list is empty. Nothing to pop.")
        else:
            print(f"Popped | Node: {popped_node} | Value: {popped_node.value}")

    elif action == "pop_first":
        popped_node = my_linked_list.pop_first()
        if popped_node is None:
            print("The linked list is empty. Nothing to pop.")
        else:
            print(f"Popped first | Node: {popped_node} | Value: {popped_node.value}")

    elif action == "get":
        try:
            index = int(input("Enter the index to get: "))
            node = my_linked_list.get(index)
            if node is None:
                print(f"No node found at index {index}.")
            else:
                print(f"Got | Node: {node} | Value: {node.value}")
        except ValueError:
            print("Please enter a valid integer index.")

    elif action == "set":
        try:
            index = int(input("Enter the index to set: "))
            new_value = input("Enter the new value: ")
            node = my_linked_list.set(index, new_value)
            if node:
                print(f"Set | Node: {node} | Value: {node.value}")
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
            node = my_linked_list.insert(index, new_value)
            if node:
                print(f"Inserted | Node: {my_linked_list.get(index)} | Value: {my_linked_list.get(index).value}")
            else:
                print(f"Failed to insert {new_value} at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "remove":
        try:
            index = int(input("Enter the index to remove: "))
            node = my_linked_list.remove(index)
            if node is not None:
                print(f"Removed | Node: {node} | Value: {node.value}")
            else:
                print(f"Failed to remove value at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "reverse":
        my_linked_list.reverse()
        print("Reversed the linked list.")
        my_linked_list.print_list()
        
    elif action == "findmiddle":
        middle_node = my_linked_list.find_middle_node()
        if middle_node is not None:
            print(f"Middle Node: {middle_node} | Value: {middle_node.value}")
        else:
            print("The linked list is empty. No middle node found.")
            
    elif action == "hasloop":
        has_loop = my_linked_list.has_loop()
        if has_loop:
            print("The linked list has a loop.")
        else:
            print("The linked list does not have a loop.")

    elif action == "findkthfromend":
        try:
            k = int(input("Enter the value of k (1-based index from the end): "))
            kth_node = my_linked_list.find_kth_node_from_end(k)
            if kth_node is not None:
                print(f"Kth Node from End: {kth_node} | Value: {kth_node.value}")
            else:
                print(f"No node found at position {k} from the end.")
        except ValueError:
            print("Please enter a valid integer for k.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "remove_duplicates":
        my_linked_list.remove_duplicates()
        print("Removed duplicates from the linked list.")
        my_linked_list.print_list()

    else:
        print("Invalid action. Please choose print, append, pop, pop_first, prepend, get, set, insert, remove, reverse, findmiddle, hasloop, findkthfromend, remove_duplicates, or quit.")
