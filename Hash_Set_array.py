"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-08-13"
-------------------------------------------------------
"""
# pylint: disable=protected-access
# 8 functions in the Hash Set - Once you Finish this and BSTs make sure to practice your other stuff.
# make sure youre ready for this final.
# Imports
# Use any appropriate data structure here.
from List_array import List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(List())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        # your code here

        slot = self._table[key]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        contains = False
        for hash_set in self._table:
            for element in hash_set:
                if element == key:
                    contains = True
        return contains

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        if value == type(str):
            value = ord(value)
        contains = False
        hash_value = value % self._capacity
        if value in self._table[hash_value]:
            contains = True
        if contains is False:
            self._table[hash_value].append(value)
            self._count += 1
        if self._count / self._capacity > self._LOAD_FACTOR:
            self._rehash()
        return contains

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        value = None
        hash_key = key % self._capacity
        if key in self._table[hash_key]:
            value = key
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        value = None
        hash_key = key % self._capacity
        key_removal = self._table[hash_key]
        if key in key_removal:
            value = key
            key_removal.remove(key)
            self._count -= 1
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        new_capacity = self._capacity * 2 + 1
        new_table = [[] for _ in range(new_capacity)]
        for slot in self._table:
            if slot:
                for element in slot:
                    new_hash_value = element % new_capacity
                    new_table[new_hash_value].append(element)
        self._table = new_table
        self._capacity = new_capacity
        return

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # your code here
        equals = False
        if self._table[:] == target[:]:
            equals = True
        return equals

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        print("{} Slots:".format(self._capacity))
        for i in range(len(self._table)):
            print("Slot {}:".format(i))
            print()
            for j in self._table[i]:
                print(j)

        return

    def cipher(self, string):
        # turns a string into its hash value
        scrambled = ""
        for c in string:
            scrambled = scrambled + str(ord(c)) + " "

        return scrambled[:-1]

    def decipher(self, string):
        # turns a hash value string into normal letters
        unscrambled = ""
        str_list = string.split()
        for i in str_list:
            unscrambled += chr(int(i))
        return unscrambled

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item


h = Hash_Set(1)
h.insert(1)
h.insert(3)
h.insert(4)
h.insert(5)
h.insert(6)
h.insert(7)
h.insert(8)
h.insert(9)
h.insert(10)
h.insert(11)

h._rehash()

for slot in h:
    print(slot)
