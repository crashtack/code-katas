import sys
from stack import Stack


def matcher(string, closers):

    pairs = int(len(closers) / 2)

    shit_is_good = True

    for i in range(0, pairs):
        print('i: {}'.format(i))
        start = i * 2
        end = start + 2
        closer = closers[start:end]

        stk = Stack()
        for char in string:
            # import pdb; pdb.set_trace()
            if char == closer[0]:
                stk.push(char)
            if char == closer[1]:
                try:
                    stk.pop()
                except IndexError:
                    shit_is_good = False
                    break
        try:
            stk.pop()
            shit_is_good = False
        except IndexError:
            shit_is_good = True

        i += 1

    return shit_is_good



if __name__ == "__main__":
    sting = sys.argv[1]
    closers = sys.argv[2]

    print(matcher(sting, closers))
