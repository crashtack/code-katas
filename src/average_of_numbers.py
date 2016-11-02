def averages(arr):
    output = []

    for i in range(len(arr or []) - 1):
        output.append(sum(arr[i: i + 2]) / float(2))

    return output
