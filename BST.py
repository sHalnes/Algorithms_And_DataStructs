#  the key in each node must be greater than or equal to any key stored in the left sub-tree,
# and less than or equal to any key stored in the right sub-tree.

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


class BinaryTree:
    def __init__(self, cargo):
        self.bin_tree = Tree(cargo)

    def get_root(self):
        return self.bin_tree

    def add_leaf(self, new_leaf):
        new_branch = Tree(new_leaf)
        current_node = self.bin_tree
        while True:
            if new_leaf >= current_node.cargo:
                if current_node.right == None:
                    current_node.right = new_branch
                    return
                else:
                    current_node = current_node.right
            else:
                if current_node.left == None:
                    current_node.left = new_branch
                    return
                else:
                    current_node = current_node.left


                    # tree = BinaryTree(20)
                    # tree.add_leaf(25)
                    # tree.add_leaf(9)
                    # tree.add_leaf(40)
                    # tree.add_leaf(12)
                    # tree.add_leaf(5)
                    # tree.add_leaf(11)
                    # tree.add_leaf(14)