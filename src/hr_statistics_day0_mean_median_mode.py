def mean(lst):
    """Return the mean of a list"""
    result = 0.0
    total = 0
    for i in lst:
        total += i
    result = total / len(lst)
    return result


def median(lst):
    """Return the medain of a list"""
    lst.sort()
    output = 0
    if len(lst) % 2 == 0:
        output = (lst[(int(len(lst) / 2)) - 1] + lst[int(len(lst) / 2)]) / 2
    else:
        if len(lst) == 1:
            output = lst[0]
        else:
            output = lst[int(len(lst) / 2)]

    output = float('{:0.1f}'.format(output))
    print(output)
    return output


def mode():
    """Return the mode of a list"""
    pass


if __name__ == "__main__":
    n = input().strip()
    n = n.split(',')
    print(n)
    lst = []
    for i in n:
        lst.append(int(i))
    median(lst)
