"""
-------------------------------------------------------
linked version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-08-03"
-------------------------------------------------------
"""
from copy import deepcopy
# this module contains the code to make self rotate like on the midterm.


class _PQ_Node:

    def __init__(self, value, _next):
        """
        -------------------------------------------------------
        Initializes a priority queue node that contains a copy of value
        and a link to the next node in the priority queue
        Use: node = _PQ_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _next - another priority queue node (_PQ_Node)
        Returns:
            a new Priority_Queue object (_PQ_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = _next


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """

        # Your code here

        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """

        # Your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is inserted into the priority queue.
        Values are stored in priority order. 
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # Your code here
        value = deepcopy(value)
        current = self._front
        previous = None
        index = 0

        while current is not None and current._value < value:
            index += 1
            previous = current
            current = current._next

        if previous is not None:
            new_node = _PQ_Node(value, current)
            previous._next = new_node
            if current is None:
                self._rear = new_node

        else:
            new_node = _PQ_Node(value, current)
            self._front = new_node
            if current is None:
                self._rear = new_node

        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot remove from an empty priority queue"

        # Your code here
        value = self._front._value
        self._front = self._front._next
        self._count -= 1
        if self._count == 1:
            self._rear = self._front
        if self._count < 1:
            self._rear = None
            self._front = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty priority queue"

        # Your code here
        value = deepcopy(self._front._value)
        return value

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        # Your code here
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        slow = self._front  # [1,2,3,4,5] = 1
        fast = None

        if slow is not None:
            fast = self._front._next

        while fast is not None or slow is not None:
            if slow is not None:
                current1 = target1._front
                previous1 = None
                while current1 is not None:
                    previous1 = current1
                    current1 = current1._next
                if previous1 is not None:
                    new_node = deepcopy(slow)
                    new_node._next = current1
                    previous1._next = new_node
                    if current1 is None:
                        target1._rear = new_node
                else:
                    new_node = deepcopy(slow)
                    new_node._next = current1
                    target1._front = new_node
                    if current1 is None:
                        target1._rear = new_node
                target1._count += 1

            if fast is not None:
                current2 = target2._front
                previous2 = None
                while current2 is not None:
                    previous2 = current2
                    current2 = current2._next
                if previous2 is not None:
                    new_node = deepcopy(fast)
                    new_node._next = current2
                    previous2._next = new_node
                    if current2 is None:
                        target2._rear = new_node
                else:
                    new_node = deepcopy(fast)
                    new_node._next = current2
                    target2._front = new_node
                    if current2 is None:
                        target2._rear = new_node
                target2._count += 1

            if slow is not None:
                slow = slow._next
                if slow is not None:
                    slow = slow._next

            if fast is not None:
                fast = fast._next
                if fast is not None:
                    fast = fast._next

        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = pq1.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        # Your code here
        current = self._front
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        while current is not None and current._value < key:
            current1 = target1._front
            previous1 = None
            while current1 is not None:
                previous1 = current1
                current1 = current1._next
            if previous1 is not None:
                new_node = deepcopy(current)
                new_node._next = current1
                previous1._next = new_node
                if current1 is None:
                    target1._rear = new_node
            else:
                new_node = deepcopy(current)
                new_node._next = current1
                target1._front = new_node
                if current1 is None:
                    target1._rear = new_node
            target1._count += 1
            current = current._next

        while current is not None and current._value >= key:
            current2 = target2._front
            previous2 = None
            while current2 is not None:
                previous2 = current2
                current2 = current2._next
            if previous2 is not None:
                new_node = deepcopy(current)
                new_node._next = current2
                previous2._next = new_node
                if current2 is None:
                    target2._rear = new_node
            else:
                new_node = deepcopy(current)
                new_node._next = current2
                target2._front = new_node
                if current2 is None:
                    target2._rear = new_node
            target2._count += 1
            current = current._next

        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are inserted 
        into target and source1 and source2 are empty. Order is preserved
        with source1 elements having priority over source2 elements with the
        same priority value.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked priority queue (Priority_Queue)
            source2 - a linked priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        current_source1 = source1._front
        current_source2 = source2._front
        while current_source1 is not None or current_source2 is not None:
            if current_source1 is not None:
                current1 = self._front
                previous1 = None
                while current1 is not None:
                    previous1 = current1
                    current1 = current1._next
                if previous1 is not None:
                    new_node = deepcopy(current_source1)
                    new_node._next = current1
                    previous1._next = new_node
                    if current1 is None:
                        self._rear = new_node
                else:
                    new_node = deepcopy(current_source1)
                    new_node._next = current1
                    self._front = new_node
                    if current1 is None:
                        self._rear = new_node
                self._count += 1
                current_source1 = current_source1._next

            if current_source2 is not None:
                current1 = self._front
                previous1 = None
                while current1 is not None:
                    previous1 = current1
                    current1 = current1._next
                if previous1 is not None:
                    new_node = deepcopy(current_source2)
                    new_node._next = current1
                    previous1._next = new_node
                    if current1 is None:
                        self._rear = new_node
                else:
                    new_node = deepcopy(current_source2)
                    new_node._next = current1
                    self._front = new_node
                    if current1 is None:
                        self._rear = new_node
                self._count += 1
                current_source2 = current_source2._next

        source1._front = None
        source1._rear = None
        source1._count = 0
        source2._front = None
        source2._rear = None
        source2._count = 0
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty priority queue"
        # Your code here
        self._rear._next = source._front
        self._rear = source._front
        self._count += source._count
        source._front = None
        source._rear = None
        source._count = None
        return

    def _append_queue_sorted(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to target queue.
        The source queue becomes empty. self may NOT be empty.
        if this is the case, you must append the values
        in source in priority order compared to self.

        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        if self._front is None:
            while source._front is not None:
                self._move_front_to_rear(source)
        else:
            current_source2 = source._front
            current1 = self._front
            previous1 = None

            while current1 is not None:
                previous1 = current1
                current1 = current1._next
            if previous1 is not None:
                new_node = deepcopy(current_source2)
                new_node._next = current1
                previous1._next = new_node
                if current1 is None:
                    self._rear = new_node
            else:
                new_node = deepcopy(current_source2)
                new_node._next = current1
                self._front = new_node
                if current1 is None:
                    self._rear = new_node
            self._count += 1
            current_source2 = current_source2._next

        # in the case you also want to cycle through self and make it rotate like on
        # the midterm, this is how you would have to do it. self._count is
        # the number of times it is rotating in this case.
        for _ in range(self._count-1):
            self._move_front_to_rear(self)

        return

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated. Order is preserved.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty priority queue"
        # Your code here
        front = source._front
        source._front = source._front._next
        rear = self._rear

        if self._front is not None:
            rear._next = front
            self._rear = rear._next
            self._rear._next = None
        else:
            self._front = front
            self._rear = self._front
            self._rear._next = None

        self._count += 1

        if source._front is None:
            source._rear = source._front
        source._count -= 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
