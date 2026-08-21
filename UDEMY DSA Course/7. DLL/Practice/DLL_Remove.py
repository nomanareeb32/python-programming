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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" <--> ")
            temp = temp.next
        print("None")

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

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

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
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


value = input("Enter the value for the head of the doubly linked list: ")
dll = DoublyLinkedList(value)

while True:
    action = input("\nWhat would you like to do? (append/pop/prepend/pop_first/print_list/get/set_value/insert/remove/quit): ").lower()

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

    elif action == "pop_first":
        popped_node = dll.pop_first()
        if popped_node:
            print(f"Popped First | Node: {popped_node} | Value: {popped_node.value}")
        else:
            print("The doubly linked list is empty. Nothing to pop.")

    elif action == "print_list":
        print("Doubly Linked List:")
        dll.print_list()
    
    elif action == "get":
        index = int(input("Enter the index of the node to get: "))
        node = dll.get(index)
        if node:
            print(f"Node ({node}) at index {index}: {node.value}")
        else:
            print("Index out of bounds.")

    elif action == "set_value":
        index = int(input("Enter the index of the node to set: "))
        value = input("Enter the new value: ")
        if dll.set_value(index, value):
            print(f"Value at index {index} updated successfully.")
        else:
            print("Index out of bounds.")

    elif action == "insert":
        index = int(input("Enter the index where you want to insert the node: "))
        value = input("Enter the value for the new node: ")
        if dll.insert(index, value):
            print(f"Node inserted at index {index}.")
        else:
            print("Index out of bounds.")

    elif action == "remove":
        index = int(input("Enter the index of the node to remove: "))
        removed_node = dll.remove(index)
        if removed_node:
            print(f"Removed | Node: {removed_node} | Value: {removed_node.value}")
        else:
            print("Index out of bounds.")

    else:
        print("Invalid action. Please choose append, pop, prepend, pop_first, print_list, get, set_value, insert, remove, or quit.")
