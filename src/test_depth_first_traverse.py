import pytest
from depth_first_traverse import dft, bft
from bst import BST

DTF_TABLE = [
    ([1], [1]),
    ([2, 1, 3], [2, 1, 3]),
    ([4, 2, 1, 3, 5, 6, 7], [4, 2, 1, 3, 5, 6, 7])
]


BFT_TABLE = [
    ([1], [1]),
    ([2, 1, 3], [2, 1, 3]),
    ([4, 2, 1, 3, 6, 5, 7], [4, 2, 6, 1, 3, 5, 7])
]


@pytest.mark.parametrize('in_list, result', DTF_TABLE)
def test_dft(in_list, result):
    """
    Test that the depth first travers returns a list in the
    correct order
    """
    bst = BST()
    out_list = []
    for i in in_list:
        bst.insert(i, 0)
    for i in dft(bst):
        out_list.append(i)
    assert out_list == result


@pytest.mark.parametrize('in_list, result', BFT_TABLE)
def test_bft(in_list, result):
    """
    Test that the bredth first travers returns a list in the
    correct order
    """
    bst = BST()
    out_list = []
    for i in in_list:
        bst.insert(i, 0)
    for i in bft(bst):
        out_list.append(i)
    assert out_list == result
