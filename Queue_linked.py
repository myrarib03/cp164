"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author: Myra Ribeiro
ID:     169030590
Email:  ribe0590@mylaurier.ca
__updated__ = "2024-08-14"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Queue:
    """
    A linked Queue class.
    """

    def consecutive_sums(self):
        """
        ---------------------------------------------------------
        Sums consecutive elements with equal values and replaces value in 
        first node with that sum. Excess nodes are removed.
        Use: queue.consecutive_sums()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            None
        ---------------------------------------------------------
        """
        # Your code here
        sum = 0
        current1 = self._front
        while current1 is not None:
            if current1 is not None and current1._next is not None and current1._value == current1._next._value:
                sum = current1._value
                sum += current1._next._value

                current = self._front
                found = False
                previous = None
                index = -1
                while found is False and current is not None:
                    index += 1
                    if current._value == current1._value:
                        found = True
                    else:
                        previous = current
                        current = current._next

                if found is False:
                    index = -1
                    previous = self._rear
                    current = None
                if index != -1:
                    if previous is not None:
                        previous._next = current._next
                        if previous._next is None:
                            self._rear = previous
                    else:
                        self._front = current._next
                    self._count -= 1
                    if self._count == 1:
                        self._rear = self._front
                    if self._front is None:
                        self._rear = None

            current1 = current1._next
            if current1 is not None and current1._next is not None and current1._next._value != current1._value:
                current1._value = sum
                sum = 0

        return

    def rotate(self, n):
        """
        -------------------------------------------------------
        Rotates position of nodes in source, moving nodes
        from front to rear n times.
        n must be >= 0.
        Use: source.rotate(n)
        -------------------------------------------------------
        Parameters:
            n - The number of nodes to be rotated. (int >= 0)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        assert n >= 0, "n must be >= 0"
        # Your code here
        if self._count != 0 or n > 0:
            n = n % self._count
            for _ in range(n):
                self._front = self._front._next
                self._rear = self._rear._next
        return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        ---------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            a new Queue object (Queue)
        ---------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        node = _Queue_Node(value, None)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Queue_Node:
    """
    A linked Queue Node class.
    """

    def __init__(self, value, next_):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        ---------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
