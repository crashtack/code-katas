import sys
import os


def sum2(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    print(total)
    return total

if __name__ == "__main__":

    print(sum2([1, 2, 3, 4]))
