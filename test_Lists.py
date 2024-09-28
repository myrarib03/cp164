"""
-------------------------------------------------------
Exam: Simple List testing

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
from List_linked import List


# Constants
VALUES0 = (3, 8, 9, 7, 6, 2, 4, 6,)
VALUES1 = (4, 2, 7, 5, 0,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies List values to a Python list.
    """
    values = []
    for value in source:
        values.append(value)
    return values


def to_List(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_split_alt_many():
    """
    Tests the 'split_alt_many' method.
    """
    print(SEP)
    print("Test 'split_alt_many'")
    print()

    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    targets = source.split_alt_many(1)
    print("targets = source.split_alt_many(1)")

    for i in range(len(targets)):
        print(f"  targets[{i}]: {to_python_list(targets[i])}")
    print()
    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    targets = source.split_alt_many(3)
    print("targets = source.split_alt_many(1)")

    for i in range(len(targets)):
        print(f"  targets[{i}]: {to_python_list(targets[i])}")
    print()


def test_common_node():
    """
    Tests the 'common_node' method.
    """
    print(SEP)
    print("Test 'common_node'")
    print()
    source = to_List(VALUES0)
    print(f"source: {to_python_list(source)}")
    target = to_List(VALUES1)
    print(f"target: {to_python_list(target)}")
    node = source.common_node(target)
    print("node = source.common_node(target)")

    if node is None:
        print("node: None")
    else:
        print(f"node: {node._value}")
    print()
    # Connect target List to source List
    target._front._next._next = source._front._next._next
    print(f"source: {to_python_list(source)}")
    print(f"target: {to_python_list(target)}")
    node = source.common_node(target)
    print("node = source.common_node(target)")

    if node is None:
        print("node: None")
    else:
        print(f"node: {node._value}")


if __name__ == "__main__":
    """
    Remove Comment '#' from functions to test
    """
    print("List_linked Testing")
    test_split_alt_many()
    test_common_node()
