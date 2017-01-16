def print_number(dic, name):
    num = dic.setdefault(name)
    if num:
        message = "{}={}".format(name, num)
        print(message)
        return message
    else:
        message = "Not found"
        print(message)
        return message


if __name__ == "__main__":
    dic = {}

    num = int(input().strip())

    for i in range(num):
        entry = input().strip().split(" ")
        name = entry[0]
        number = int(entry[1])
        dic.setdefault(name, number)

    while True:
        query = input().strip()
        print_number(dic, query)
