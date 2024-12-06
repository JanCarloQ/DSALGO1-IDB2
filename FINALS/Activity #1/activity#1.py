from LinkedDeque import LinkedDeque
from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack


D = LinkedDeque()
Q = LinkedQueue()
S = LinkedStack()


D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("Contents of deque D:", D)
print("Contents of Queue Q:", Q)


for _ in range(4):
    Q.enqueue(D.delete_first())
    print("Contents of deque D:", D)
    print("Contents of Queue Q:", Q)


for _ in range(3):
    D.insert_last(Q.dequeue())
    print("Contents of deque D:", D)
    print("Contents of Queue Q:", Q)


D.insert_last(D.delete_first())
print("Contents of deque D:", D)
print("Contents of Queue Q:", Q)


while not Q.is_empty():
    D.insert_last(Q.dequeue())
    print("Contents of deque D:", D)
    print("Contents of Queue Q:", Q)


for _ in range(3):
    Q.enqueue(D.delete_first())
    print("Contents of deque D:", D)
    print("Contents of Queue Q:", Q)


for _ in range(3):
    D.insert_last(Q.dequeue())
    print("Contents of deque D:", D)
    print("Contents of Queue Q:", Q)


while not D.is_empty():
    D.delete_first()


D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print()
print()
print("Contents of deque D:", D)
print("Contents of Stack S:", S)


for _ in range(3):
    S.push(D.delete_first())
    print("Contents of deque D:", D)
    print("Contents of Stack S:", S)


S.push(D.delete_first())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)

S.push(D.delete_first())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)


D.insert_first(S.pop())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)

D.insert_last(S.pop())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)

S.push(D.delete_first())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)

S.push(D.delete_last())
print("Contents of deque D:", D)
print("Contents of Stack S:", S)

while not S.is_empty():
    D.insert_first(S.pop())
    print("Contents of deque D:", D)
    print("Contents of Stack S:", S)



