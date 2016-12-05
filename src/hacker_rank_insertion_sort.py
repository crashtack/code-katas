def insertion_sort(arr):
    try:
        value = arr[-1]
    except IndexError:
        return []

    for i in range(1, len(arr) + 1):
        if value < arr[-(i + 1)]:
            arr[-i] = arr[-(i + 1)]
        else:
            arr[-i] = value
            break
        a = [print(arr[x], end=' ') for x in range(len(arr))]
        print()
    a = [print(arr[x], end=' ') for x in range(len(arr))]
    return arr


if __name__ == "__main__":
    length = str(input())
    array = input()
    arr = array.split(' ')
    arr = [int(arr[x]) for x in range(len(arr))]
    insertionSort(arr)
