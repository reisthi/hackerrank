# Python3 program to find the maximum depth of tree


class Node:
    def __init__(self, data):
        self.root = data
        self.right = None
        self.left = None


def max_depth(node):
    if node is None:
        return -1
    else:
        left_depth = max_depth(node.left)
        right_node = max_depth(node.right)

        return (left_depth + 1) if left_depth > right_node else (right_node + 1)
