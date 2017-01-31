"""
    Binary Search Tree:
        Methods:
            - insert
            - delete
            - size
            - root
            - contains
            - depth
            - balance
"""


class Node(object):
    """ The BST Node object """

    def __init__(self, key=None, value=None, left=None, right=None):
        """ Node initialization """
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def insert(self, new_node):
        """ Insert a node into a tree """
        if new_node.key > self.key:
            if self.right:
                self.right.insert(new_node)
            else:
                self.right = new_node

        elif new_node.key < self.key:
            if self.left:
                self.left.insert(new_node)
            else:
                self.left = new_node


class BST(object):
    """ The BST object """

    def __init__(self):
        """ Initialize an empty BST """
        self.root = None
        self.size = 0

    def insert(self, key, value=None):
        """ Create a new node with the given key and value """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self.root.insert(key, value)
        self.size += 1
