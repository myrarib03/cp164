"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2024-08-14"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class CircularQueue:

    def __init__(self):
        self.front = None  # Points to the front node of the queue
        self.rear = None   # Points to the rear node of the queue
        self.size = 0      # Number of elements in the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        new_node = _Queue_Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        value = self.front.value
        if self.front == self.rear:  # Only one element in the queue
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        self.size -= 1
        return value

    def peek(self):
        """Return the element at the front of the queue without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.value

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def display(self):
        """Display the elements of the queue."""
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        while True:
            print(current.value, end=" ")
            current = current.next
            if current == self.front:
                break
        print()

    def rotate(self, k):
        """Rotate the circular queue k times."""
        if self.is_empty() or k <= 0:
            return

        k = k % self.size  # Effective rotations
        for _ in range(k):
            self._front = self._front._next
            self._rear = self._rear._next
