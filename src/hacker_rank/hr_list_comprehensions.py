def cuboid(X, Y, Z, N):
    output = [x for x in range(X) if x != N]
    print(output)
    return output

if __name__ == "__main__":
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())

    cuboid(X, Y, Z, N)
