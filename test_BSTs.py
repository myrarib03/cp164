"""
-------------------------------------------------------
Exam: Simple BST testing

See main code at bottom
Remove '#' from lines to test
-------------------------------------------------------
Author: Myra Ribeiro
ID:     169030590
Email:  ribe0590@mylaurier.ca
__updated__ = "2024-08-15"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
VALUES0 = (11, 7, 6, 9, 8, 15, 12, 18,)
VALUES1 = (2, 3, 1,)
SEP = '-' * 60


def to_python_list(source):
    """
    Testing helper method. Copies BST values to a Python list in levelorder
    """
    return source.levelorder()


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    bst = BST()

    for v in values:
        bst.insert(v)
    return bst


def test_right_turn():
    """
    Tests the '_right_turn' method.
    """
    print(SEP)
    print("Test '_right_turn'")
    print("(BST shown in level order)")
    print()

    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    source._root = source._right_turn(source._root)
    print("source._root = source._right_turn(source._root)")
    print(f"source: {to_python_list(source)}")
    print()
    print(f"source: {to_python_list(source)}")
    source._root._right = source._right_turn(source._root._right)
    print("source._root._right = source._right_turn(source._root._right)")
    print(f"source: {to_python_list(source)}")
    print()


def test_total_height():
    """
    Tests the 'total_height' method.
    """
    print(SEP)
    print("Test 'total_height'")
    print("(BST shown in level order)")
    print()

    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    th = source.total_height()
    print("th = source.total_height()")
    print(f"th: {th}")
    print()
    source = to_BST(VALUES1)
    print(f"source: {to_python_list(source)}")
    th = source.total_height()
    print("th = source.total_height()")
    print(f"th: {th}")
    print()


def test_max_path():
    """
    Tests the 'max_path' method.
    """
    print(SEP)
    print("Test 'max_path'")
    print("(BST shown in level order)")
    print()

    source = to_BST(VALUES0)
    print(f"source: {to_python_list(source)}")
    mp = source.max_path()
    print("mp = source.max_path()")
    print(f"mp: {mp}")
    print()
    source = to_BST(VALUES1)
    print(f"source: {to_python_list(source)}")
    mp = source.max_path()
    print("mp = source.max_path()")
    print(f"mp: {mp}")
    print()


if __name__ == "__main__":
    """
    Remove Comment '#' from functions to test
    """
    print("BST_linked Testing")
    test_right_turn()
    test_total_height()
    test_max_path()
