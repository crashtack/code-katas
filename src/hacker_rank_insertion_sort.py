def insertion_sort(arr):
    try:
        value = arr[-1]
    except IndexError:
        return []

    for i in range(len(arr) - 1, 0, -1):
        if i == 1 and value < arr[i - 1]:
            arr[1] = arr[0]
            a = [print(arr[x], end=' ') for x in range(len(arr))]
            print()
            arr[0] = value
            break
        elif value < arr[i - 1]:
            arr[i] = arr[i - 1]
        else:
            arr[i] = value
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
