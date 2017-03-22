def bar(items):
    for i in items:
        print(i)
        print("Hello? Is there anyone home? {}".format(i))


create hash
add element
delet element
hashing_func


def hashing_func(obj, size):
    return obj % size


def create_hash(size):
    table = [ll(), ]
    return table


def add_element(table, element):
    index = hashing_func(element, size)
    if table[index].contains(element):
        return table
    else:
        table[hashing_func(element, size)].append(element)
        return table


def delete_element(table, element, size):
    index = hasing_func(element, size)
    if table[index].contains(element):
        table[index].delete(element)
        return table
    else:
        return table


if __name__ == "__main__":
    bar(["fred", "dave"])
