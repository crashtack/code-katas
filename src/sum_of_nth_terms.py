def series_sum(n):
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
