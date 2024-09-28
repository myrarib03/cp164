"""
-------------------------------------------------------
[BST Practice Questions]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2024-08-13"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

"""
Problem 33: Find Pairs with Given Sum in a BST
Given a binary search tree and a target sum, find all pairs of nodes in the tree 
whose sum equals the given target.
"""


def target_sum(bst, target):
    """
    finds all pairs of nodes in a BST whose sum equals
    that of a given target.
    """
    new_list = bst.inorder()
    counts = 0
    for i in range(new_list-1):
        if i+1 < len(new_list) and new_list[i] + new_list[i+1] == target:
            counts += 1
    return counts


"""
Problem 31: check if a given list of integers represents
a valid preorder traversal of a BST
"""


def valid_preorder(bst, lists):
    """
    Given a list of integers, determine if it represents a valid preorder traversal of a BST.
    """


"""
problem 30: merge two BSTs into a sorted list or an unknown number
"""


def merge_bst_list(root1, root2):
    """
    Given two BSTs, merge them into a single sorted list.
    """


def merge_bst_to_list(unknown_num):
    """
    given a list of a unknown number of BSTs merge them all into 
    one list of integers
    """


"""
Problem 30: Merge Two Balanced BSTs
Given two balanced binary search trees, merge them into a single balanced binary search tree. 
The merged tree should maintain the BST property and should be as balanced as possible.
"""


def merge_bst_to_bst(bst1, bst2):
    """
    Given two balanced binary search trees, merge them into a single balanced binary search tree. 
    The merged tree should maintain the BST property and should be as balanced as possible.
    """


"""
Convert BST to dequeue
"""


def convert_bst_dequeue(bst):
    """
    converts BST to a dequeue
    """
