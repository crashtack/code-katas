def conditional(arr):
    """Print stuff based on input arr"""
    if arr % 2:
        return "Weird"
    elif arr % 2 == 0 and 2 <= arr <= 5:
        return "Not Weird"
    elif not arr % 2 and 2 <= arr <= 20:
        return "Weird"
    elif not arr % 2 and arr > 20:
        return "Not Weird"


if __name__ == "__main__":
    N = int(input().strip())
    print(conditional(N))
