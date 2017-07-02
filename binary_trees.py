class BinaryTree:

    def __init__(self):
        self.tree = []

    def __str__(self):
        return str(self.tree)

    def add_child(self, child):
        self.tree.append(child)

    def get_children(self, index):
        ch1 = 2*index + 1
        ch2 = 2*index + 2
        return (self.tree[ch1] if ch1 < len(self.tree) else None), \
               (self.tree[ch2] if ch2 < len(self.tree) else None)

    def get_parent(self, index):
        parent = int((index-1)/2)
        return self.tree[parent]

# tree_elements = [7, 1, 10, 4, 6, 9, 2, 11, 3, 5, 12, 8]
# bin_tree = BinaryTree()
# for element in tree_elements:
#     bin_tree.add_child(element)
# print('Binary tree: ', bin_tree)
# print('\nParent for node 1: ', bin_tree.get_parent(1))
# print('Children for node 1: ', bin_tree.get_children(1))
# print('\nParent for node 9: ', bin_tree.get_parent(5))
# print('Children for node 9: ', bin_tree.get_children(5))
# print('\nChildren for node 6: ', bin_tree.get_children(4))
# print('\nChildren for node 2: ', bin_tree.get_children(6))
# print('\nParent for node 7: ', bin_tree.get_parent(0))
