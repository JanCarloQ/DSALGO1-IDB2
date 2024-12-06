class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    #---------------- nested _Node class ----------------
    class _Node:
        '''Lightweight non public class for storing a singly linked node.'''
        __slots__ = '_element', '_next' # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #--------------- queue methods ----------------
    def __init__(self):
        '''Create an empty queue'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''Return true if the queue is empty.'''
        return self._size == 0
    def first(self):
        '''Return but do not remove the element at the fron of the queue'''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element #front aligned with the head of the list

    def dequeue(self):
        '''Remove and return the first element of the queue (FIFO)'''
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next  # Fixed this line
        self._size -= 1
        if self.is_empty():  # Special case: queue is empty
            self._tail = None  # Removed head had been the tail
        return answer
    def enqueue(self, e):
        '''Add an element to the back of queue.'''
        newest = self._Node(e, None)#node will be new tail node
        if self.is_empty():
            self._head = newest#special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest#update reference to tail node
        self._size += 1

    def __str__(self):
        elements = []
        current = self._header._next  # Start with the first real element
        while current != self._trailer:  # Until we reach the trailer node
            elements.append(str(current._element))  # Add element to list
            current = current._next  # Move to the next node
        return f"({', '.join(elements)})"  # Join elements with commas, enclosed in parentheses

    def __str__(self):
        '''Return a string representation of the queue's elements.'''
        elements = []
        current = self._head  # Start with the head of the list
        while current is not None:  # Traverse until the end
            elements.append(str(current._element))  # Add element to list
            current = current._next  # Move to the next node
        return f"({', '.join(elements)})"  # Join elements with commas, enclosed in parentheses
