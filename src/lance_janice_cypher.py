import sys


def decode(string):
    out_string = ''
    for char in string:
        if char.islower():
            out_string += chr(-(ord(char)) + 219)
        else:
            out_string += char
    return out_string


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    if len(sys.argv) == 2 and type(sys.argv[1]) == str:
        print(decode(sys.argv[1]))

    else:
        string = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
        print(decode(string))
