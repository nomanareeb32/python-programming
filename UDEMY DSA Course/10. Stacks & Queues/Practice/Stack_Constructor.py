class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

try:
    value = int(input("Enter a value to initialize the stack: "))
    my_stack = Stack(value)

    print('Top:', my_stack.top.value)
    print('Height:', my_stack.height)
    
except ValueError:
    print("Invalid input. Please enter an integer value.")
