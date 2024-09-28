"""
-------------------------------------------------------
Exam: Simple Deques testing

See main code at bottom
Remove '#' from lines to test
-------------------------------------------------------
Author: Myra Ribeiro
ID:     169030590
Email:  ribe0590@mylaurier.ca
__updated__ = "2024-08-15"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Deque_linked import Deque

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (8, 6, 7, 2, 7, 6, 8,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Deque values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Deque(values):
    """
    Testing helper method. Copies Python list values to a Deque.
    """
    source = Deque()
    for value in values:
        source.insert_front(value)
    return source


def test_is_mirror():
    """
    Tests the 'is_mirror' method.
    """
    print(SEP)
    print("Test 'is_mirror'")
    print()

    source = to_Deque(VALUES0)
    print(f"source: {to_python_list(source)}")
    mirror = source.is_mirror()
    print(f"mirror = source.is_mirror()")
    print(f"mirror: {mirror}")
    print()
    source = to_Deque(VALUES1)
    print(f"source: {to_python_list(source)}")
    mirror = source.is_mirror()
    print(f"mirror = source.is_mirror()")
    print(f"mirror: {mirror}")
    print()


def test_split_alt():
    """
    Tests the 'split_alt' method.
    """
    print(SEP)
    print("Test 'split_alt'")
    print()

    source = to_Deque(VALUES0)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_alt()
    print(f"target1, target2 = source.split_alt()")
    print(f"target1: {to_python_list(target1)}")
    print(f"target2: {to_python_list(target2)}")
    print()
    source = to_Deque(VALUES1)
    print(f"source: {to_python_list(source)}")
    target1, target2 = source.split_alt()
    print(f"target1, target2 = source.split_alt()")
    print(f"target1: {to_python_list(target1)}")
    print(f"target2: {to_python_list(target2)}")
    print()


if __name__ == "__main__":
    print("Deque_linked Testing")
    test_is_mirror()
    test_split_alt()
