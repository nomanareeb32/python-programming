class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
            
try:
    value = int(input("Enter a value to initialize the stack: "))
    my_stack = Stack(value)

    print('Top:', my_stack.top.value)
    print('Height:', my_stack.height)
    
except ValueError:
    print("Invalid input. Please enter an integer value.")

while True:
    action = input("\nWhat would you like to do? (push/pop/print/quit): ").lower()
    
    if action == "quit":
        break

    elif action == "push":
        try:
            value = int(input("Enter a value to push onto the stack: "))
            my_stack.push(value)
            print('Top:', my_stack.top.value)
            print('Height:', my_stack.height)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    elif action == "pop":
        if my_stack.height == 0:
            print("Stack is empty. Cannot pop.")
        else:
            popped_value = my_stack.top.value
            my_stack.top = my_stack.top.next
            my_stack.height -= 1
            print(f"Popped value: {popped_value}")
            if my_stack.height > 0:
                print('New Top:', my_stack.top.value)
            else:
                print('Stack is now empty.')
            print('Height:', my_stack.height)
