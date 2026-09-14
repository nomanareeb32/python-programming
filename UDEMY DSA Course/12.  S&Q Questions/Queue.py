class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def print_queue(self):
        print("Queue elements:")
        for i in range(len(self.stack1)-1, -1, -1):
            print(self.stack1[i])

    def is_empty(self):
        return len(self.stack1) == 0

    def enqueue(self, value):
        # transfer stack1 → stack2
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        
        # push new value onto stack1 (it's now empty)
        self.stack1.append(value)
        
        # transfer stack2 → stack1
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.stack1.pop()