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

    def print_list(self):
        temporary_node = self.head
        if temporary_node is None:
            print("The doubly linked list is empty.")
            return
        while temporary_node is not None:
            print(f"Node: {temporary_node} | Value: {temporary_node.value}")
            temporary_node = temporary_node.next

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
        return True

    def pop(self):
        if self.length == 0:
            return None
        temporary_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temporary_node.prev = None
        self.length -= 1
        return temporary_node

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
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temporary_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temporary_node.next = None
        self.length -= 1
        return temporary_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temporary_node = self.head
        for _ in range(index):
            temporary_node = temporary_node.next
        return temporary_node

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
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return new_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temporary_node = self.get(index)
        temporary_node.prev.next = temporary_node.next
        temporary_node.next.prev = temporary_node.prev
        temporary_node.next = None
        temporary_node.prev = None
        self.length -= 1
        return temporary_node

    def reverse(self):
        if self.length <= 1:
            return
        temporary_node = self.head
        self.head = self.tail
        self.tail = temporary_node
        while temporary_node is not None:
            temporary_node.next, temporary_node.prev = temporary_node.prev, temporary_node.next
            temporary_node = temporary_node.prev

    # def reverse(self):
    #         if not self.head or not self.head.next:
    #             return
    #         current = self.head
    #         temp = None
    #         while current:
    #             temp = current.prev
    #             current.prev = current.next
    #             current.next = temp
    #             current = current.prev
    #         temp = self.head
    #         self.head = self.tail
    #         self.tail = temp

    def is_palindrome(self):
        if self.length <= 1 or self.head == self.tail:
            return True
        left = self.head
        right = self.tail
        while left != right and left.prev != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True

    def partition(self, x):
        if self.length == 0:
            print("The doubly linked list is empty. Nothing to partition.")
            return
        less_dll = DoublyLinkedList(0)    # dummy head with value 0
        greater_dll = DoublyLinkedList(0) # dummy head with value 0
        temporary_node = self.head
        while temporary_node is not None:
            if temporary_node.value < x:
                less_dll.append(temporary_node.value)
            else:
                greater_dll.append(temporary_node.value)
            temporary_node = temporary_node.next
        # connect less chain to greater chain (skip dummy heads)
        less_real_head = less_dll.head.next    # first real less node
        greater_real_head = greater_dll.head.next  # first real greater node
        if less_real_head is None:
            # no less values — list is just the greater partition
            self.head = greater_real_head
            self.tail = greater_dll.tail
        elif greater_real_head is None:
            # no greater values — list is just the less partition
            self.head = less_real_head
            self.tail = less_dll.tail
        else:
            # connect less tail to greater head
            less_dll.tail.next = greater_real_head
            greater_real_head.prev = less_dll.tail

            self.head = less_real_head
            self.tail = greater_dll.tail
        # fix head's prev pointer
        if self.head is not None:
            self.head.prev = None

value = input("Enter the head for the new doubly linked list: ")
dll = DoublyLinkedList(value)


while True:
    action = input("\nWhat would you like to do? (print/append/pop/pop_first/prepend/get/set/insert/remove/reverse/check_palindrome/partition/quit): ").lower()

    if action == "quit":
        print("Exiting program.")
        break

    elif action == "print":
        dll.print_list()

    elif action == "append":
        new_value = input("Enter the value to append: ")
        dll.append(new_value)
        print(f"Appended | Node: {dll.tail} | Value: {dll.tail.value}")

    elif action == "prepend":
        new_value = input("Enter the value to prepend: ")
        dll.prepend(new_value)
        print(f"Prepended | Node: {dll.head} | Value: {dll.head.value}")

    elif action == "pop":
        popped_node = dll.pop()
        if popped_node is None:
            print("The doubly linked list is empty. Nothing to pop.")
        else:
            print(f"Popped | Node: {popped_node} | Value: {popped_node.value}")

    elif action == "pop_first":
        popped_node = dll.pop_first()
        if popped_node is None:
            print("The doubly linked list is empty. Nothing to pop.")
        else:
            print(f"Popped first | Node: {popped_node} | Value: {popped_node.value}")

    elif action == "get":
        try:
            index = int(input("Enter the index to get: "))
            node = dll.get(index)
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
            node = dll.set(index, new_value)
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
            node = dll.insert(index, new_value)
            if node:
                print(f"Inserted | Node: {dll.get(index)} | Value: {dll.get(index).value}")
            else:
                print(f"Failed to insert {new_value} at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "remove":
        try:
            index = int(input("Enter the index to remove: "))
            node = dll.remove(index)
            if node is not None:
                print(f"Removed | Node: {node} | Value: {node.value}")
            else:
                print(f"Failed to remove value at index {index}.")
        except ValueError:
            print("Please enter a valid integer index.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "reverse":
        dll.reverse()
        print("Reversed the doubly linked list.")
        dll.print_list()

    elif action == "check_palindrome":
        is_palindrome = dll.is_palindrome()
        print(f"Is the doubly linked list a palindrome? {is_palindrome}")

    elif action == "partition":
        try:
            x = int(input("Enter the partition value: "))
            dll.partition(x)
            print(f"Partitioned the doubly linked list around value {x}.")
            dll.print_list()
        except ValueError:
            print("Please enter a valid integer for partitioning.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid action. Please choose print, append, pop, pop_first, prepend, get, set, insert, remove, reverse, check_palindrome, partition, or quit.")