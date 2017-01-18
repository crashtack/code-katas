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


def quartiles(data):
    """
        Return the Qurtile Q1, Q2, Q3 in a list
        based on the inputed list of data
    """
    data.sort()
    # print("data: {}".format(data))
    q2 = median(data)

    # print("lower half: {}".format(data[:int(len(data) / 2)]))
    q1 = median(data[:int(len(data) / 2)])

    if len(data) % 2 == 0:
        q3 = median(data[int(len(data) / 2):])
    else:
        # print("upper half: {}".format(data[int(len(data) / 2) + 1:]))
        q3 = median(data[int(len(data) / 2) + 1:])

    result = [q1, q2, q3]
    # print(result)
    return result


if __name__ == "__main__":
    input()
    data = input().strip()
    n1 = data.split(' ')
    lst = []
    for i in n1:
        lst.append(int(i))

    for i in quartiles(lst):
        print(int(i))

    # quartiles([3, 7, 8, 5, 12, 14, 21, 13, 18])
