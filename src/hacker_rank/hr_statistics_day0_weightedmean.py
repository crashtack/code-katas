def weighted_mean(lst, weight):
    """
        Return the weight mean based on a list of values
        and a list of weights for the values
    """
    output = 0
    total = 0
    divisor = 0
    for i in range(len(lst)):
        total += lst[i] * weight[i]
        divisor += weight[i]
    output = total / divisor
    return float('{:0.1f}'.format(output))


if __name__ == "__main__":
    input()

    n1 = input().strip()
    import pdb; pdb.set_trace()
    n1 = n1.split(' ')
    lst = []
    for i in n1:
        lst.append(int(i))

    n2 = input().strip()
    n2 = n2.split(' ')
    weight = []
    for i in n2:
        weight.append(int(i))

    print(weighted_mean(lst, weight))
