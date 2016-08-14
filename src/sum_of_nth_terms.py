def series_sum(n):
    ''' sum of the nth series:
        Series: 1  1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
        Examples:
            series_sum(1) => 1 = "1"
            series_sum(2) => 1 + 1/4 = "1.25"
            series_sum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
    '''

    # print('n = {}'.format(n))
    out = 1
    if n == 0:
        return '0.00'
    if n == 1:
        return '1.00'
    else:
        for i in range(2, n + 1):
            # print('range(n): {}'.format(i))
            out += 1 / ((i * 2) + (i - 2))
        return('{:.2f}'.format(out))


def series_sum2(n):
    return '{:.2f}'.format(sum(1.0 / (i * 3 + 1) for i in range(n)))


def series_sum3(n):
    amount = 0
    for i in range(n):
        amount += 1.0 / (i * 3 + 1)
    return '{:.2f}'.format(amount)

print(series_sum3(5))
