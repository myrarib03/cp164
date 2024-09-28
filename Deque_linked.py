"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author: Myra Ribeiro
ID:     169030590
Email:  ribe0590@mylaurier.ca
__updated__ = "2024-08-15"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Deque:
    """
    Defines a linked Deque.
    """

    def is_mirror(self):
        """
        -------------------------------------------------------
        Determines if a Deque is mirrored, i.e. the left half
        and right half contain the same values in opposite order.
        Use: mirror = source.is_mirror()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            mirror - True if source is mirrored, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        mirror = True
        if self._count > 1:
            slow = self._front
            fast = self._front
            if self._front is not None:
                while fast is not None and fast._next is not None:
                    fast = fast._next._next
                    if fast is not None:
                        slow = slow._next
            front = self._front
            rear = self._rear
            while front != slow:
                if front._value != rear._value:
                    mirror = False
                front = front._next
                rear = rear._prev
        return mirror

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source Deque into two separate target Deques by moving
        alternating nodes into the target Deques. At finish source is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            target1 - contains alternating values from source (Deque)
            target2 - contains other alternating values from source (Deque)
        -------------------------------------------------------
        """
        # your code here
        slow = self._front
        fast = self._front._next
        target1 = Deque()
        target2 = Deque()

        while slow is not None and slow._next is not None:
            new_slow = deepcopy(slow)
            if target1._front is None:
                target1._rear = new_slow
            else:
                target1._front._prev = new_slow
            target1._front = new_slow
            target1._count += 1
            slow = slow._next._next

        while fast is not None and fast._next is not None:
            new_fast = deepcopy(fast)
            if target2._front is None:
                target2._rear = new_fast
            else:
                target2._front._prev = new_fast
            target2._front = new_fast
            target2._count += 1
            fast = fast._next._next

        return target1, target2

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = Deque()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, self._front)

        if self._front is None:
            self._rear = node
        else:
            self._front._prev = node
        self._front = node
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, self._rear, None)

        if self._rear is None:
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
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Deque_Node:
    """
    Defines a linked Deque node.
    """

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns‌​‌​​​​‌​​‌‌​​‌‌​​‌‌‌​‌‌‌‌‌​:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next
