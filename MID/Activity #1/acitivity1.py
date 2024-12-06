class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

print("First Simulation")
stack = Stack()
stack.push(5)
print("After S.push(5):",stack)
stack.push(3)
print("After S.push(3):",stack)
print("Length of the stock:", len(stack))
print("Returned: ", stack.pop())
print("Is the stock empty?:", stack.is_empty())
print("After S.is_empty():",stack)
print("Returned: ", stack.pop())
print("After S.pop():",stack)
print("Is the stock empty?:", stack.is_empty())
print("Returned:", stack.pop())
stack.push(7)
print("After S.push(7):",stack)
stack.push(9)
print("After S.push(9):",stack)
stack.top()
print("After S.top():",stack)
stack.push(4)
print("After S.push(4):",stack)
print("Length of the stock:", len(stack))
print("Returned:", stack.pop())
print("After S.pop:",stack)
stack.push(6)
print("After S.push(6):",stack)
stack.push(8)
print("After S.push(8):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)

print()
print()
print("Second Simulation")
stack = Stack()
stack.push(5)
print("After S.push(5):",stack)
stack.push(3)
print("After S.push(3):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
stack.push(2)
print("After S.push(2):",stack)
stack.push(8)
print("After S.push(8):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
stack.push(9)
print("After S.push(9):",stack)
stack.push(1)
print("After S.push(1):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
stack.push(7)
print("After S.push(7):",stack)
stack.push(6)
print("After S.push(6):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
stack.push(4)
print("After S.push(4):",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
print("Returned:", stack.pop())
print("After S.pop:",stack)
