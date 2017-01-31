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
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
        self.size += 1

    def contains(self, key):
        """ Returns True if BST contains given key """
        current = self.root
        while True:
            if current is None:
                return False
            elif key == current.key:
                return True
            elif key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
