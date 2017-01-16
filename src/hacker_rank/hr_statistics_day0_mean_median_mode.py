def mean(lst):
    """Return the mean of a list"""
    result = 0.0
    total = 0
    for i in lst:
        total += i
    result = total / len(lst)
    return float('{:0.1f}'.format(result))


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
    return output


def mode(lst):
    """Return the mode of a list"""
    lst.sort()
    mode_ = None
    max_count = 0
    count = 1
    last = None
    for i in lst:
        if i == last:
            count += 1
        else:
            count = 1
        if count > max_count:
            mode_ = i
        max_count = max(max_count, count)
        last = i
        count = 1

    return mode_


if __name__ == "__main__":
    input()
    n = input().strip()
    n = n.split(' ')
    lst = []
    for i in n:
        lst.append(int(i))

    print(mean(lst))
    print(median(lst))
    print(mode(lst))
