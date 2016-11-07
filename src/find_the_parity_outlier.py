def find_outlier(integers):
    evencount = 0
    for i in range(3):
        if (integers[i] % 2) == 0:
            evencount += 1
    if evencount >= 2:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
