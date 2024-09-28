"""
-------------------------------------------------------
Linked version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-08-03"
-------------------------------------------------------
"""
from copy import deepcopy


class _Stack_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a stack node that contains a copy of value
        and a link to the next node in the stack.
        Use: node = _Stack_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Stack node (_Stack_Node)
        Returns:
            a new _Stack_Node object (_Stack_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Values are stored in a 
        linked structure.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._top = None

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = stack.is_empty()
        -------------------------------------------------------
        Returns:
            True if stack is empty, False otherwise
        -------------------------------------------------------
        """
        # your code here
        return self._top is None

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: stack.push(value)
        -------------------------------------------------------
        Parameters:
            value - value to be added to stack (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        value = deepcopy(value)
        value = _Stack_Node(value, self._top)
        self._top = value
        return

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = stack.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot pop from an empty stack"
        # your code here
        value = self._top._value
        self._top = self._top._next
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = stack.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of stack (?)
        -------------------------------------------------------
        """
        assert self._top is not None, "Cannot peek at an empty stack"
        # your code here
        value = deepcopy(self._top._value)
        return value

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: stack.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        current = self._top
        previous = None
        next_node = 0
        counts = 0
        stored_top = self._top

        while stored_top is not None:
            counts += 1
            first_value = stored_top
            stored_top = stored_top._next
        # [1,2], top = 1, next = 2, previous = none
        if counts > 1:
            while current is not None and next_node is not None:
                next_node = current._next  # next_node = 2
                if next_node is not None:
                    current._next = previous  # 1_node_next = None
                    self._top = next_node  # new_top = 2
                    nexts = next_node._next  # nexts = None
                    next_node._next = current  # 2._next is 1
                    previous = next_node  # 2
                    current = nexts  # our new current value is None
                    # our past value which is 2 (which now points to 1 and is our top)
            top = self._top
            self._top = first_value
            first_value._next = top

        return

    def _move_top(self, source):
        """
        -------------------------------------------------------
        Moves the top node from the source stack to the target stack.
        The target stack contains the old top node of the source stack.
        The source stack top is updated. Equivalent of
        self.push(source.pop()), but moves nodes, not data.
        Use: target._move_top(source)
        -------------------------------------------------------
        Parameters:
        source - a linked stack (Stack)
        Returns:
        None
        ------
        """
        # your code here
        if source._top is not None:

            new_node = source._top  # store our source top
            source._top = source._top._next  # set our new source top
            new_node._next = self._top  # set our next top value
            self._top = new_node  # set our self top

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked stack (Stack)
            source2 - an linked stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self._top = None

        while source1._top is not None or source2._top is not None:
            if source1._top is not None and source2._top is not None:
                self._move_top(source1)
                self._move_top(source2)
            elif source1._top is not None and source2._top is None:
                self._move_top(source1)
            elif source2._top is not None and source1._top is None:
                self._move_top(source2)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values 
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        # your code here
        target1 = Stack()
        target2 = Stack()
        while self._top is not None:
            target1._move_top(self)
            target2._move_top(self)
        return target1, target2

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            _value - the next value in the stack (?)
        -------------------------------------------------------
        """
        current = self._top

        while current is not None:
            yield current._value
            current = current._next
