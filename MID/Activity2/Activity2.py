class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def first(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


print("First Simulation")
Q = Queue()
Q.enqueue(5)
print("After Q.enqueue(5):", Q)
Q.enqueue(3)
print("After Q.enqueue(3):", Q)
print("Length of the Queue:",len(Q))
Q.dequeue()
print("After dequeue:", Q)
print("Is queue empty?", Q.is_empty())
Q.dequeue()
print("After dequeue:", Q)
print("Is queue empty?", Q.is_empty())
Q.dequeue()
print("After dequeue:", Q)
Q.enqueue(7)
print("After Q.enqueue(7):", Q)
Q.enqueue(9)
print("After Q.enqueue(9):", Q)
print("First element:", Q.first())
Q.enqueue(4)
print("After Q.enqueue(4):", Q)
print("Length of the Queue:",len(Q))
Q.dequeue()
print("After dequeue:", Q)


print()
print()
print("Second Simulation")
Q = Queue()
Q.enqueue(5)
print("After Q.enqueue(5):", Q)
Q.enqueue(3)
print("After Q.enqueue(3):", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.enqueue(2)
print("After Q.enqueue(2):", Q)
Q.enqueue(8)
print("After Q.enqueue(8):", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.enqueue(9)
print("After Q.enqueue(9):", Q)
Q.enqueue(1)
print("After Q.enqueue(1):", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.enqueue(7)
print("After Q.enqueue(7):", Q)
Q.enqueue(6)
print("After Q.enqueue(6):", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.enqueue(4)
print("After Q.enqueue(4):", Q)
Q.dequeue()
print("After dequeue:", Q)
Q.dequeue()
print("After dequeue:", Q)