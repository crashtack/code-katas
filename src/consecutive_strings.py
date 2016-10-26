"""
    Codewars.com
    Consecutive Strings

    You are given an array strarr of strings and an integer k. Your task is to
    return the first longest string consisting of k consecutive strings taken
    in the array.
    Example:
    longest_consec(["zone", "abigail", "theta", "form",
                    "libe", "zas", "theta", "abigail"],
                     2) --> "abigailtheta"
    n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
"""


def longest_consec(strarr, k):
    longest = ''
    for pos in range(len(strarr) - (k - 1)):   # len()
        length = ''.join(strarr[pos:pos + k])
        if len(longest) < len(length):
            longest = length
    return longest
