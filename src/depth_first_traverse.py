from stack import Stack
from queue_ import Queue


def dft(bst):
    """
    Return the Pre-order (depth first traverse) traversal
    of a Binary Search Tree
    """
    s = Stack()
    s.push(bst.root)
    while s.size():
        x = s.pop()
        if x:
            s.push(x.right)
            s.push(x.left)
            yield(x.value)


def bft(bst):
    """
    Return Bredth first traversal of a Binary
    serch tree
    """
    q = Queue()
    q.enqueue(bst.root)
    while q.size():
        x = q.dequeue()
        if x:
            q.enqueue(x.left)
            q.enqueue(x.right)
            yield(x.value)
