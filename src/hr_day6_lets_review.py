def review(arr):
    """for given string print even-indexed characters, a space,
       then odd-indexed characters.
    """
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[i], end="")

    print(" ", end='')

    for i in range(len(arr)):
        if i % 2 == 1:
            print(arr[i], end="")

    print()


if __name__ == "__main__":
    cases = int(input())

    for i in range(cases):
        review(input())
