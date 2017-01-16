class Stack(object):

    def __init__(self, input=None):
        self.lst = []

    def pop(self):
        """pops the vlaue of the top of the stack"""
        return self.lst.pop()

    def push(self, val):
        """pushes a value onto the top of the stack"""
        return self.lst.append(val)

    def size(self):
        '''returns the size of the linked list'''
        return len(self.lst)


def int_to_binary(integer):
    """
        Convert base 10 integer to base 2
    """

    output = []
    binary = Stack()
    remainder = 0

    while integer > 0:
        remainder = integer % 2
        binary.push(remainder)
        integer = int(integer / 2)

    while binary.size():
        output.append(binary.pop())
    return output


def consecutive_ones(lst):
    """
        Returns the maximum number of concecutive 1's in a give
        list of integers
    """
    max_ones = 0
    current = 0

    for i in lst:
        if i == 1:
            current += 1
            if current > max_ones:
                max_ones = current
        else:
            current = 0

    return max_ones


if __name__ == "__main__":
    n = int(input().strip())
    print(consecutive_ones(int_to_binary(n)))
