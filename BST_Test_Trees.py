"""
-------------------------------------------------------
[BST Test Trees]
-------------------------------------------------------
Author:  Myra Ribeiro
ID:      169030590
Email:   ribe0590@mylaurier.ca
__updated__ = "2024-08-13"
-------------------------------------------------------
"""
# Imports

# Constants

"""
BST Test Trees:
"""
"""
        3
    1        5
0    2    4    6
"""
# [3,1,5,0,2,4,6]
#tree1 = BST()
"""
        2
    3
"""
"""
BST:
                       60
         45                        70
    40          48             67         80
39     41    47     50      66    68    79   81

"""
# [60,45,70,40,48,67,80,39,41,47,50,66,68,79,81]
#tree2 = BST()

"""
          11
              22 
                  33
                      44
"""
# [11,22,33,44]
#tree3 = BST()

"""
values_to_insert = [3, 1, 5, 0, 2, 4, 6]
for value in values_to_insert:
    tree.insert(value)
"""

"""Rotate function (left):
        10
       /   \
      5      20
     / \    /  \
    3   7  15   30
       /   / \
      6   12  18
becomes...
        20
       /  \
     10    30
    /  \ 
   5   15  
  / \   / \
 3   7 12 18
    /
   6
"""

"""Rotate function (right):
        10
       /   \
      5     20
     / \   /  \
    3   7 15   30
       /  / \
      6  12  18

becomes...
          5
        /    \
       3     10
            /   \
           7     20
          /     /  \
        6     15   30
            /   \
            12  18

"""
#[10, 5, 20, 3, 7, 15, 30, 6, 12, 18]


from BST_linked import BST
tree = BST()

values_to_insert = [10, 5, 20, 3, 7, 15, 30, 6, 12, 18]

for value in values_to_insert:
    tree.insert(value)

print(tree.inorder())
print(tree.morris_traversal())
