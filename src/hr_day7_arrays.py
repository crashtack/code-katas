def reverse_list(arr):
    """Print the input list in reverse order"""
    arr = arr[::-1]
    [print(x, end=' ') for x in arr]
    print()
    return arr


if __name__ == "__main__":
    num = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    print("ouput: {}".format(reverse_list(arr)))
