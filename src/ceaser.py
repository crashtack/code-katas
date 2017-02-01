""" Ceaser Cypher

    function to return a string where each letter is
    shifted n places down the alpabit

"""


def ceaser(message=None, shift=None):
    """ Ceaser Cypher:
            Returns shifted message
            Changes to all lower Case
            Ignores punctuation
    """
    if message is None or shift is None:
        return None
    else:
        message = message.lower()
        output = ''
        for i in message:
            ord_i = ord(i)
            if 97 <= ord_i <= 122:
                ord_i -= 98
                ord_i += shift
                ord_i = ord_i % 26
                output += chr(ord_i + 98)
            else:
                output += ' '
    print("mesaage: {} output: {}".format(message, output))
    return output
