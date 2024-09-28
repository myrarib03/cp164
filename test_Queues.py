"""
-------------------------------------------------------
Exam: Simple Queues testing

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
from Queue_linked import Queue

# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (3, 3, 7, 4, 4, 4, 5,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies Queue values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_Queue(values):
    """
    Testing helper method. Copies Python list values to a Queue.
    """
    source = Queue()
    for value in values:
        source.insert(value)
    return source


def test_consecutive_sums():
    """
    Tests the 'consecutive_sums' method.
    """
    print(SEP)
    print("Test 'consecutive_sums'")
    print()

    source = to_Queue(VALUES0)
    print(f"source: {to_python_list(source)}")
    source.consecutive_sums()
    print("source.consecutive_sums()")
    print(f"source: {to_python_list(source)}")
    print()
    source = to_Queue(VALUES1)
    print(f"source: {to_python_list(source)}")
    source.consecutive_sums()
    print("source.consecutive_sums()")
    print(f"source: {to_python_list(source)}")
    print()


def test_rotate():
    """
    Tests the 'rotate ' method.
    """
    print(SEP)
    print("Test 'rotate '")
    print()

    source = to_Queue(VALUES0)
    print(f"source: {to_python_list(source)}")
    source.rotate(0)
    print("source.rotate (0)")
    print(f"source: {to_python_list(source)}")
    print()
    source = to_Queue(VALUES0)
    print(f"source: {to_python_list(source)}")
    source.rotate(3)
    print("source.rotate (3)")
    print(f"source: {to_python_list(source)}")
    print()
    source = to_Queue(VALUES0)
    print(f"source: {to_python_list(source)}")
    source.rotate(12)
    print("source.rotate (12)")
    print(f"source: {to_python_list(source)}")
    print()


if __name__ == "__main__":
    """
    Remove Comment '#' from functions to test
    """
    print("Queue_linked Testing")
    test_consecutive_sums()
    test_rotate()
