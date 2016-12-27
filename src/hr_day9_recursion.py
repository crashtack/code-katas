def factorial(N):
    """Return the factorial of N using recursion"""
    if N <= 1:
        return 1
    else:
        return N * factorial(N - 1)


if __name__ == "__main__":
    print(factorial(int(input().strip())))
