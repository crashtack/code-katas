def merge_sorted_lists(l1, l2):
    """Merge two sorted lists"""
    ml = []
    while l1 and l2:
        if l1[0] > l2[0]:
            ml.append(l2.pop(0))
        else:
            ml.append(l1.pop(0))
    return ml + l1 + l2
