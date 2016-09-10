# -*- coding: utf-8 -*-


def smart_substr(str, terminate='...'):
    if len(str) < 30:
        return str
    str = str[:30]
    print(str)
    print(len(str))
    words = str.split()
    print(words)
    print(len(words))
    outstring = ''
    for index in range(len(words) - 2):
        outstring += words[index] + " "
    outstring += words[index + 1]
    return outstring + terminate


def smart_substr2(str, terminate='...'):
    if len(str) < 30:
        return str
    str = str[:30]

    words = str.rsplit(maxsplit=1)
    print('28', str[28:])
    print('bla: ', str[len(words[0]):])
    # if words[1] = str[-(len(words):]:

    print(words)
    print(len(words))

    return words[0] + terminate


def smart_substr3(str, terminate='...'):
    if len(str) < 30:
        return str
    str = str[:30]
    words = str.rsplit(maxsplit=1)
    return words[0] + terminate


test_string = 'this is a very long string. with a bunch of extra words blaaa blass eeck'
print('output: {}'.format(smart_substr2(test_string)))
