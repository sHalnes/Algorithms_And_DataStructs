from BST import *

''' Find largest smallest BST key. Return -1 if there is no such number'''

def find_largest_smallest(root, n):
    result = -1
    while root is not None:
        if root.cargo < n:
            result = root.cargo
            root = root.right
        else:
            root = root.left
    return result




tree = BinaryTree(20)
tree.add_leaf(25)
tree.add_leaf(9)
tree.add_leaf(40)
tree.add_leaf(12)
tree.add_leaf(5)
tree.add_leaf(11)
tree.add_leaf(14)

root = tree.get_root()
n = 27
print(find_largest_smallest(root, n))