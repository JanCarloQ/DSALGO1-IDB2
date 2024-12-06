from LinkedQueue import LinkedQueue
from LinkedStack import LinkedStack

# Initialize a queue for the front and a stack for the back
front_queue = LinkedQueue()
back_stack = LinkedStack()


def is_empty():
    '''Return True if the deque is empty.'''
    return front_queue.is_empty() and back_stack.is_empty()


def add_first(e):
    '''Add element e to the front of the deque.'''
    front_queue.enqueue(e)


def add_last(e):
    '''Add element e to the back of the deque.'''
    back_stack.push(e)


def remove_first():
    '''Remove and return the first element from the deque.'''
    if front_queue.is_empty():
        raise Exception("Deque is empty!")
    return front_queue.dequeue()


def remove_last():
    '''Remove and return the last element from the deque.'''
    if back_stack.is_empty():
        raise Exception("Deque is empty!")
    return back_stack.pop()


def first():
    '''Return (but do not remove) the first element of the deque.'''
    if front_queue.is_empty():
        raise Exception("Deque is empty!")
    return front_queue.first()


def last():
    '''Return (but do not remove) the last element of the deque.'''
    if back_stack.is_empty():
        raise Exception("Deque is empty!")
    return back_stack.top()


def __str__():
    '''Return a string representation of the deque contents.'''
    elements = []

    # Collect elements from front queue
    temp_queue = LinkedQueue()
    while not front_queue.is_empty():
        element = front_queue.dequeue()
        elements.append(element)
        temp_queue.enqueue(element)

    # Restore front queue
    while not temp_queue.is_empty():
        front_queue.enqueue(temp_queue.dequeue())

    # Collect elements from back stack
    temp_stack = LinkedStack()
    while not back_stack.is_empty():
        element = back_stack.pop()
        elements.append(element)
        temp_stack.push(element)

    # Restore back stack
    while not temp_stack.is_empty():
        back_stack.push(temp_stack.pop())

    return "Deque: [" + ", ".join(map(str, elements)) + "]"


# Create a variable D to use for the deque operations
class D:
    @staticmethod
    def add_first(e):
        add_first(e)

    @staticmethod
    def add_last(e):
        add_last(e)

    @staticmethod
    def remove_first():
        return remove_first()

    @staticmethod
    def remove_last():
        return remove_last()

    @staticmethod
    def first():
        return first()

    @staticmethod
    def last():
        return last()

    @staticmethod
    def is_empty():
        return is_empty()

    def __str__(self):
        return __str__()


# Create an instance of D
D = D()

# Example usage
if __name__ == "__main__":
    D.add_first(1)
    D.add_last(2)
    D.add_first(0)
    print(D)