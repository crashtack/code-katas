def loop(arr):
    """Return the first 10 multiples of arr"""
    for i in range(1, 11):
        output = "{} x {} = {}".format(arr, i, arr * i)
        print(output)

if __name__ == "__main__":
    arr = int(input().strip())
    loop(arr)
