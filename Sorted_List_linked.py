"""
-------------------------------------------------------
Linked version of the Sorted_List ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-08-13"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _SL_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a sorted list node.
        Use: node = _SL_Node(value, next_)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            next_ - another sorted list node (_SL_Node)
        Returns:
            Initializes a list node that contains a copy of value
            and a link to the next node in the list.
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
        return


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: sl = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = sl.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here

        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the list.
        Use: n = len(l)
        -------------------------------------------------------
        Returns:
            Returns the number of values in the list.
        -------------------------------------------------------
        """

        # your code here

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in the sorted list.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: sl.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """

        # your code here
        # check to see if value is already in list
        previous, current, index = self._linear_search(value)

        if index == -1:
            if previous is None:
                new_node = _SL_Node(value, None)
                self._front = new_node
                self._rear = new_node

            else:
                current = self._front
                previous = None
                found_placement = False

                while current is not None and found_placement is False:
                    if current._value > value:
                        found_placement = True
                    else:
                        previous = current
                        current = current._next

                new_node = _SL_Node(value, current)

                if previous is not None:
                    previous._next = new_node
                else:
                    self._front = new_node

                if new_node._next is None:
                    self._rear = new_node

        else:
            while current is not None and current._value == value:
                previous = current
                current = current._next

            new_node = _SL_Node(value, current)
            previous._next = new_node

            if new_node._next is None:
                self._rear = new_node

        self._count += 1
        return

    def _linear_search(self, key):
        """
        Cannot do a (simple) binary search on a linked structure. 
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """

        # your code here

        current = self._front
        found = False
        previous = None
        index = -1

        while found is False and current is not None:
            index += 1
            if current._value == key:
                found = True
            else:
                previous = current
                current = current._next

        if found is False:
            index = -1
            previous = self._rear
            current = None

        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the sorted list that matches key.
        Use: value = sl.remove( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """

        # your code here
        previous, current, index = self._linear_search(key)
        value = None
        if index != -1:
            value = current._value
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
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        # your code here
        value = deepcopy(self._front._value)
        self._front = self._front._next
        if self._front is None:
            self._rear = None
        self._count -= 1

        if self._count == 1:
            self._rear = self._front
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: l.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            All values matching key are removed from the list.
        -------------------------------------------------------
        """
        # your code here

        previous, current, index = self._linear_search(key)
        if index != -1:
            counts = 0
            while current is not None and current._value == key:
                counts += 1
                current = current._next

            if previous is not None:
                previous._next = current
            else:
                self._front = current

            self._count -= counts

            if self._count == 1:
                self._rear = self._front
            if self._front is None:
                self._rear = None
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in list that matches key.
        Use: value = l.find( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here

        _, current, index = self._linear_search(key)
        value = None
        if index != -1:
            value = deepcopy(current._value)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = l.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        # your code here
        value = deepcopy(self._front._value)
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = l.index( key )
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list.
        -------------------------------------------------------
        """
        # your code here
        _, _, index = self._linear_search(key)
        return index

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        valid = False
        if -self._count < i < (self._count-1):
            valid = True

        return valid

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        current = self._front
        index = 0
        if i < 0:
            i = self._count - i

        while current is not None and index < i:
            previous = current
            current = current._next
            index += 1
        if current is not None:
            value = deepcopy(current._value)
        else:
            value = deepcopy(previous._value)
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        _, _, index = self._linear_search(key)
        if index == -1:
            contains = False
        else:
            contains = True
        return contains

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in the sorted list.
        Use: value = sl.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        # your code here
        value = deepcopy(self._rear._value)
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in the sorted list.
        Use: value = sl.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the sorted list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find minimum of an empty list"

        # your code here
        value = deepcopy(self._front._value)
        return value

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in the sorted list.
        Use: n = sl.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in the sorted list (int)
        -------------------------------------------------------
        """
        # your code here
        _, current, index = self._linear_search(key)
        counts = 0
        if index != -1:
            while current is not None and current._value == key:
                counts += 1
                current = current._next
        return counts

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here

        current = self._front
        previous = None

        while current is not None:

            if current._next is not None and current._value == current._next._value:

                previous, current, index = self._linear_search(current._value)
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

            previous = current
            current = current._next
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:
            i = args[0]

            if i < 0:
                # index is negative
                i = self._count + i
            j = 0

            while j < i:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value

        if previous is None:
            # Update the front
            self._front = current._next
        else:
            # Update any other node
            previous._next = current._next
        self._count -= 1
        return value

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        new_source1 = Sorted_List()
        for i in source1:
            previous, current, index = new_source1._linear_search(i)
            if index == -1:
                if previous is None:
                    new_node = _SL_Node(i, None)
                    new_source1._front = new_node
                    new_source1._rear = new_node
                else:
                    current = new_source1._front
                    previous = None
                    found_placement = False

                    while current is not None and found_placement is False:
                        if current._value > i:
                            found_placement = True
                        else:
                            previous = current
                            current = current._next

                    new_node = _SL_Node(i, current)

                    if previous is not None:
                        previous._next = new_node
                    else:
                        new_source1._front = new_node

                    if new_node._next is None:
                        new_source1._rear = new_node
            else:
                while current is not None and current._value == i:
                    previous = current
                    current = current._next
                new_node = _SL_Node(i, current)
                previous._next = new_node
                if new_node._next is None:
                    new_source1._rear = new_node
            new_source1._count += 1

        new_source2 = Sorted_List()
        for i in source2:
            previous, current, index = new_source2._linear_search(i)
            if index == -1:
                if previous is None:
                    new_node = _SL_Node(i, None)
                    new_source2._front = new_node
                    new_source2._rear = new_node
                else:
                    current = new_source2._front
                    previous = None
                    found_placement = False

                    while current is not None and found_placement is False:
                        if current._value > i:
                            found_placement = True
                        else:
                            previous = current
                            current = current._next

                    new_node = _SL_Node(i, current)

                    if previous is not None:
                        previous._next = new_node
                    else:
                        new_source2._front = new_node

                    if new_node._next is None:
                        new_source2._rear = new_node
            else:
                while current is not None and current._value == i:
                    previous = current
                    current = current._next
                new_node = _SL_Node(i, current)
                previous._next = new_node
                if new_node._next is None:
                    new_source2._rear = new_node
            new_source2._count += 1

        current = new_source1._front
        previous = None
        while current is not None:
            if current._next is not None and current._value == current._next._value:
                previous, current, index = new_source1._linear_search(
                    current._value)
                if index != -1:
                    if previous is not None:
                        previous._next = current._next
                        if previous._next is None:
                            new_source1._rear = previous
                    else:
                        new_source1._front = current._next
                    new_source1._count -= 1
                    if new_source1._count == 1:
                        new_source1._rear = new_source1._front
                    if new_source1._front is None:
                        new_source1._rear = None
            previous = current
            current = current._next

        current = new_source2._front
        previous = None
        while current is not None:
            if current._next is not None and current._value == current._next._value:
                previous, current, index = new_source2._linear_search(
                    current._value)
                if index != -1:
                    if previous is not None:
                        previous._next = current._next
                        if previous._next is None:
                            new_source2._rear = previous
                    else:
                        new_source2._front = current._next
                    new_source2._count -= 1
                    if new_source2._count == 1:
                        new_source2._rear = new_source2._front
                    if new_source2._front is None:
                        new_source2._rear = None
            previous = current
            current = current._next

        # your code here
        current1 = new_source1._front

        if current1 is not None and new_source2._front is not None and new_source1._count <= new_source2._count:
            _, current2, index = new_source2._linear_search(current1._value)
            if index != -1:
                while current1 is not None and current2 is not None and current1._value == current2._value:
                    previous, current, index = self._linear_search(
                        current1._value)
                    if index == -1:
                        if previous is None:
                            new_node = _SL_Node(current1._value, None)
                            self._front = new_node
                            self._rear = new_node
                        else:
                            current = self._front
                            previous = None
                            found_placement = False
                            while current is not None and found_placement is False:
                                if current._value > current1._value:
                                    found_placement = True
                                else:
                                    previous = current
                                    current = current._next
                            new_node = _SL_Node(current1._value, current)
                            if previous is not None:
                                previous._next = new_node
                            else:
                                self._front = new_node
                            if new_node._next is None:
                                self._rear = new_node
                    else:
                        while current is not None and current._value == current1._value:
                            previous = current
                            current = current._next
                        new_node = _SL_Node(current1._value, current)
                        previous._next = new_node
                        if new_node._next is None:
                            self._rear = new_node
                    self._count += 1
                    current1 = current1._next
                    current2 = current2._next

        elif current1 is not None and new_source2._front is not None and new_source1._count > new_source2._count:
            current1 = new_source2._front
            _, current2, index = new_source1._linear_search(current1._value)
            if index != -1:
                while current1 is not None and current2 is not None and current1._value == current2._value:
                    previous, current, index = self._linear_search(
                        current1._value)
                    if index == -1:
                        if previous is None:
                            new_node = _SL_Node(current1._value, None)
                            self._front = new_node
                            self._rear = new_node
                        else:
                            current = self._front
                            previous = None
                            found_placement = False
                            while current is not None and found_placement is False:
                                if current._value > current1._value:
                                    found_placement = True
                                else:
                                    previous = current
                                    current = current._next
                            new_node = _SL_Node(current1._value, current)
                            if previous is not None:
                                previous._next = new_node
                            else:
                                self._front = new_node
                            if new_node._next is None:
                                self._rear = new_node
                    else:
                        while current is not None and current._value == current1._value:
                            previous = current
                            current = current._next
                        new_node = _SL_Node(current1._value, current)
                        previous._next = new_node
                        if new_node._next is None:
                            self._rear = new_node
                    self._count += 1
                    current1 = current1._next
                    current2 = current2._next
        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if source1._front is not None and source2._front is not None:
            if source1._count < source2._count:
                _, current, index = source1._linear_search(
                    source2._front._value)
                front = source2._front

            else:
                _, current, index = source2._linear_search(
                    source1._front._value)
                front = source1._front

            while index != -1 and current is not None:
                if current._next is None or current._value != current._next._value:
                    if front._next is None or front._value != front._next._value:
                        if current._value == front._value:
                            self.insert(current._value)
                            current = current._next
                            front = front._next
                    else:
                        front = front._next
                else:
                    current = current._next

            if source2._count < source1._count:
                current = self._rear
                self._rear = source1._rear
                current._next = self._rear
                self._count += 1

            elif source1._count < source2._count:
                current = self._rear
                self._rear = source2._rear
                current._next = self._rear
                self._count += 1

        if source1._front is None and source2._front is not None:
            for i in source2:
                self.insert(i)

        if source2._front is None and source1._front is not None:
            for i in source1:
                self.insert(i)
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = Sorted_List()
        target2 = Sorted_List()
        slow = self._front
        fast = self._front._next
        odd_or_even = self._count % 2

        while fast is not None:
            slow = slow._next
            fast = fast._next
            if fast is not None:
                fast = fast._next
        current = self._front

        while current != slow and current is not None:
            target1.insert(current._value)
            current = current._next
            self._front = current

        if odd_or_even != 0 and current is not None:
            target1.insert(current._value)
            current = current._next
            self._front = current

        while current is not None:
            target2.insert(current._value)
            current = current._next
            self._front = current

        self._front = None
        self._rear = None
        self._count = 0

        return target1, target2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish self is empty.
        Use: target1, target2 = lst.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        _, _, index = self._linear_search(key)
        present = self._front
        target1 = Sorted_List()
        target2 = Sorted_List()

        if index != -1:
            while present is not None and present._value <= key:
                target1.insert(present._value)
                present = present._next

            while present is not None and present._value > key:
                target2.insert(present._value)
                present = present._next

        else:
            while present is not None and self._rear._value <= key:
                target1.insert(present._value)
                present = present._next

        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty. Order of even and odd is not significant.
        (iterative version)
        Use: even, odd = l.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even indexed elements of the list (Sorted_List)
            odd - the odd indexed elements of the list (Sorted_List)
                The List is empty.
        -------------------------------------------------------
        """
        # your code here
        even = Sorted_List()
        odd = Sorted_List()

        if self._front is not None:
            even_element = self._front
            odd_element = self._front._next
            while even_element is not None and odd_element is not None:
                even.insert(even_element._value)
                odd.insert(odd_element._value)

                even_element = even_element._next

                if even_element is not None:
                    even_element = even_element._next

                odd_element = odd_element._next
                if odd_element is not None:
                    odd_element = odd_element._next

        if self._count % 2 != 0:
            even.insert(self._rear._value)

        self._front = None
        self._rear = None
        self._count = 0

        return even, odd

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        target1 = Sorted_List()
        target2 = Sorted_List()
        slow = self._front
        fast = self._front._next
        odd_or_even = self._count % 2

        while fast is not None:
            slow = slow._next
            fast = fast._next
            if fast is not None:
                fast = fast._next
        current = self._front

        while current != slow and current is not None:
            target1.insert(current._value)
            current = current._next
            self._front = current

        if odd_or_even != 0 and current is not None:
            target1.insert(current._value)
            current = current._next
            self._front = current

        while current is not None:
            target2.insert(current._value)
            current = current._next
            self._front = current

        self._front = None
        self._rear = None
        self._count = 0
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Sorted_Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a sorted list (Sorted_List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals = True

        if self._count != target._count:
            equals = False
        elif self._front is not None:
            current1 = self._front
            current2 = target._front

            while current1 is not None and equals is True:
                if current1._value != current2._value:
                    equals = False
                current1 = current1._next
                current2 = current2._next

        return equals

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = l.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -------------------------------------------------------
        """
        # your code here
        new_list = Sorted_List()

        for i in self:
            value = deepcopy(i)
            previous, current, index = new_list._linear_search(value)
            if index == -1:
                if previous is None:
                    new_node = _SL_Node(value, None)
                    new_list._front = new_node
                    new_list._rear = new_node
                else:
                    current = new_list._front
                    previous = None
                    found_placement = False

                    while current is not None and found_placement is False:
                        if current._value > value:
                            found_placement = True
                        else:
                            previous = current
                            current = current._next
                    new_node = _SL_Node(value, current)
                    if previous is not None:
                        previous._next = new_node
                    else:
                        new_list._front = new_node
                    if new_node._next is None:
                        new_list._rear = new_node

            else:
                while current is not None and current._value == value:
                    previous = current
                    current = current._next
                new_node = _SL_Node(value, current)
                previous._next = new_node
                if new_node._next is None:
                    new_list._rear = new_node
            new_list._count += 1

        return new_list

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        current1 = source1._front
        current2 = source2._front
        turn = True

        while current1 is not None and current2 is not None:
            if turn:
                if self._front is not None:
                    temp = deepcopy(current1)
                    previous = self._rear
                    previous._next = temp
                    self._rear = temp
                    self._rear._next = None
                    self._count += 1
                else:
                    temp = deepcopy(current1)
                    self._front = temp
                    self._rear = temp
                    self._rear._next = None
                    self._count += 1
                current1 = current1._next

            else:
                temp = deepcopy(current2)
                previous = self._rear
                previous._next = temp
                self._rear = temp
                self._rear._next = None
                self._count += 1
                current2 = current2._next
            turn = not turn

        while current1 is not None:
            if self._front is not None:
                temp = deepcopy(current1)
                previous = self._rear
                previous._next = temp
                self._rear = temp
                self._rear._next = None
                self._count += 1
            else:
                temp = deepcopy(current1)
                self._front = temp
                self._rear = temp
                self._rear._next = None
                self._count += 1
            current1 = current1._next

        while current2 is not None:
            if self._front is not None:
                temp = deepcopy(current2)
                previous = self._rear
                previous._next = temp
                self._rear = temp
                self._rear._next = None
                self._count += 1
            else:
                temp = deepcopy(current2)
                self._front = temp
                self._rear = temp
                self._rear._next = None
                self._count += 1
            current2 = current2._next

        source1._front = None
        source1._rear = None
        source1._count = 0
        source2._front = None
        source2._rear = None
        source2._count = 0

        return

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_SL_Node)
            current - pointer to the node containing key (_SL_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        previous, current, index = self.linear_search_r_aux(
            None, self._front, 0, key)

        if index > self._count-1:
            index = -1

        return previous, current, index

    def linear_search_r_aux(self, previous, current, index, key):
        if current is not None:
            if current._value != key:
                previous, current, index = self.linear_search_r_aux(
                    current, current._next, index+1, key)

        return previous, current, index

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the sorted list.
        Use: sl.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        self.clean_r_aux(None, self._front)
        return

    def clean_r_aux(self, previous, current):
        if current is not None:
            if current._next is not None and current._value == current._next._value:
                previous, current, index = self._linear_search_r(
                    current._value)

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
            self.clean_r_aux(current, current._next)

        return

    def identical_r(self, rs):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. (recursive version)
        Use: b = l.identical_r(rs)
        -------------------------------------------------------
        Parameters:
            rs - another list (Sorted_List)
        Returns:
            identical - True if this list contains the same values as rs
                in the same order, otherwise False.
        -------------------------------------------------------
        """

        # your code here
        identical = self.identical_r_aux(rs, self._front, rs._front)
        return identical

    def identical_r_aux(self, rs, current1, current2):

        if current1 is None and current2 is None:
            identical = True
        elif current1 is not None and current2 is None:
            identical = False
        elif current1 is None and current2 is not None:
            identical = False
        elif current1._value != current2._value:
            identical = False
        elif self._rear._value != rs._rear._value:
            identical = False
        elif self._count != rs._count:
            identical = False

        else:
            identical = self.identical_r_aux(
                rs, current1._next, current2._next)

        return identical

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self._front = None
        self._rear = None
        self._count = 0

        self.intersection_r_aux(source1._front, source2._front)
        return

    def intersection_r_aux(self, current1, current2):
        if current1 is not None or current2 is not None:
            if current1._value == current2._value:
                if self._rear is None or self._rear._value != current1._value:
                    new_node = deepcopy(current1)
                    new_node._next = None
                    if self._rear is None:
                        self._front = new_node
                    else:
                        self._rear._next = new_node
                    self._rear = new_node
                    self._count += 1
                self.intersection_r_aux(current1._next, current2._next)

            elif current1._value < current2._value:
                self.intersection_r_aux(current1._next, current2)

            else:
                self.intersection_r_aux(current1, current2._next)

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = l.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (Sorted_List)
        -----------------------------------------------------------
        """
        # your code here
        new_list = self.copy_r_aux(Sorted_List(), self._front)
        return new_list

    def copy_r_aux(self, new_list, current):
        if current is not None:
            if new_list._front is None:
                current1 = deepcopy(current)
                new_list._front = current1
                new_list._rear = current1
                new_list._rear._next = None
                new_list._count += 1
            else:
                current1 = deepcopy(current)
                temp = new_list._rear
                temp._next = current1
                new_list._rear = current1
                new_list._rear._next = None
                new_list._count += 1

            new_list = self.copy_r_aux(new_list, current._next)
        return new_list

    def combine_r(self, rs):
        """
        -------------------------------------------------------
        Combines contents of two lists into a third.
        Use: new_list = l1.combine(rs)
        -------------------------------------------------------
        Parameters:
            rs- an linked-based List (Sorted_List)
        Returns:
            new_list - the contents of the current Sorted_List and rs
            are interlaced into new_list - current Sorted_List and rs
            are empty (Sorted_List)
        -------------------------------------------------------
        """
        # your code here
        new_list = self.combine_r_aux(
            Sorted_List(), True, self._front, rs._front)

        return new_list

    def combine_r_aux(self, new_list, turn, current1, current2):

        if turn is True and current1 is not None and current2 is not None:
            new_node = deepcopy(current1)
            new_node._next = None

            if new_list._rear is None:
                new_list._front = new_node
            else:
                new_list._rear._next = new_node

            new_list._rear = new_node
            new_list._count += 1

            new_list = self.combine_r_aux(
                new_list, not turn, current1._next, current2)

        elif turn is False and current1 is not None and current2 is not None:
            new_node = deepcopy(current2)
            new_node._next = None

            if new_list._rear is None:
                new_list._front = new_node
            else:
                new_list._rear._next = new_node

            new_list._rear = new_node
            new_list._count += 1

            new_list = self.combine_r_aux(
                new_list, not turn, current1, current2._next)

        elif turn is True and current1 is None and current2 is not None:
            new_node = deepcopy(current2)
            new_node._next = None

            if new_list._rear is None:
                new_list._front = new_node
            else:
                new_list._rear._next = new_node

            new_list._rear = new_node
            new_list._count += 1
            new_list = self.combine_r_aux(
                new_list, not turn, current1, current2._next)

        elif turn is False and current2 is None and current1 is not None:
            new_node = deepcopy(current1)

            new_node._next = None
            if new_list._rear is None:
                new_list._front = new_node
            else:
                new_list._rear._next = new_node

            new_list._rear = new_node
            new_list._count += 1
            new_list = self.combine_r_aux(
                new_list, not turn, current1._next, current2)

        elif turn is False and current2 is not None and current1 is None:
            new_node = deepcopy(current2)

            new_node._next = None
            if new_list._rear is None:
                new_list._front = new_node
            else:
                new_list._rear._next = new_node

            new_list._rear = new_node
            new_list._count += 1
            new_list = self.combine_r_aux(
                new_list, not turn, current1, current2._next)

        return new_list

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked list (List)
            source2 - an linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self.union_r_aux(source1, source2, source1._front, source2._front)
        return

    def union_r_aux(self, source1, source2, current1, current2):
        if current1 is not None:
            _, _, index = self._linear_search_r(current1._value)
            if index == -1:
                new_node = deepcopy(current1)
                new_node._next = None
                if self._rear is None:
                    self._front = new_node
                else:
                    self._rear._next = new_node

                self._rear = new_node
                self._count += 1

            self.union_r_aux(source1, source2, current1._next, current2)
        elif current2 is not None:
            _, _, index = self._linear_search_r(current2._value)
            if index == -1:
                new_node = deepcopy(current2)
                new_node._next = None
                if self._rear is None:
                    self._front = new_node
                else:
                    self._rear._next = new_node

                self._rear = new_node
                self._count += 1
            self.union_r_aux(source1, source2, current1, current2._next)
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
