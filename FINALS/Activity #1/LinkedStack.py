class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''

    # ---------------- nested _Node class ----------------
    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    # --------------- stack methods ----------------
    def __init__(self):
        '''Create an empty Stack'''
        self._head = None  # Head points to the top of the stack (first element)
        self._tail = None  # Tail points to the last element in the stack
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the stack'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0

    def push(self, e):
        '''Add element e to the end of the stack (tail).'''
        new_node = self._Node(e)
        if self.is_empty():
            self._head = new_node  # If stack is empty, head points to the new node
            self._tail = new_node  # Tail also points to the new node
        else:
            self._tail._next = new_node  # Add the new node to the end (tail)
            self._tail = new_node  # Update the tail pointer to the new node
        self._size += 1

    def top(self):
        '''Return but do not remove the element at the top of the stack.'''
        '''Raise exception if the stack is empty.'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element  # Top of the stack is still at the head of the list

    def pop(self):
        '''Remove and return the element from the tail of the stack (LIFO).'''
        '''Raise exception if the stack is empty.'''
        if self.is_empty():
            raise Exception("The stack is empty!")

        # Special case when there's only one element in the stack
        if self._size == 1:
            answer = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            return answer

        # Traverse the list to find the second-to-last node
        current = self._head
        while current._next is not self._tail:
            current = current._next

        # Now current is the second-to-last node
        answer = self._tail._element  # Get the last element
        self._tail = current  # Update the tail to the second-to-last node
        self._tail._next = None  # Remove reference to the old tail
        self._size -= 1
        return answer

    def __str__(self):
        '''Return a string representation of the stack's elements.'''
        elements = []
        current = self._head  # Start with the head of the list
        while current is not None:  # Traverse until the end
            elements.append(str(current._element))  # Add element to list
            current = current._next  # Move to the next node
        return f"({', '.join(elements)})"
