"""
    Which of the following sorting algorithms has the best
    asymptotoc runtime complexity?
    * Buble sorting ***
    * Heap Sort`
    * Selection Sort
    * Insertion Sort

"""


def stair_case(n):
    """
        print n - i spaces, and n #
        execpt for the bottom row,
        print n #
    """
    for i in range(1, n + 1):
        if i == n:
            print("#" * n)
        else:
            print(" " * (n - i), end="")
            print("#" * i)


if __name__ == "__main__":

    stair_case(6)
