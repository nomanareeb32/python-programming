class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()

    def is_empty(self):
        return len(self.stack_list) == 0

    @staticmethod
    def reverse_string(string):
        stack = Stack()
        reversed_string = ""
        for char in string:
            stack.push(char)
        while not stack.is_empty():
            reversed_string += stack.pop()
        return reversed_string


    def is_balanced_parentheses(parentheses_string):
        stack = Stack()
        for i_p in parentheses_string:
            if i_p == "()":
                stack.push(i_p)
            elif i_p == ")":
                if stack.is_empty() or stack.pop() != "(":
                    return False
        return stack.is_empty()

my_string = 'hello'

print (Stack.reverse_string(my_string))