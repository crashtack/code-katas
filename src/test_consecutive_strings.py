import pytest
from consecutive_strings import longest_consec


# Test.describe("longest_consec")
# Test.it("Basic tests")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
# testing(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
# testing(longest_consec([], 3), "")
# testing(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
# testing(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
# testing(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "wkppixoyx3452zzzzzzzzzzzz")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
# testing(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")


PAR_TABLE = [
    ([], 3, ""),
    (["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3, "ixoyx3452zzzzzzzzzzzz"),
    (["zone", "abigail", "theta", "form", "libe", "zas"], 2, "abigailtheta"),
    (["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1, "oocccffuucccjjjkkkjyyyeehh"),
    (["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15, ""),
    (["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0, ""),
]


@pytest.mark.parametrize('strarr, k, result', PAR_TABLE)
def test_longest_consec(strarr, k, result):
    # import pdb; pdb.set_trace()
    assert longest_consec(strarr, k) == result
