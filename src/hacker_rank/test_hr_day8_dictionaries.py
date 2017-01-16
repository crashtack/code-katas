from hr_day8_dictionaries import print_number


def test_return_number_true():
    dic = {}
    dic.setdefault("harry", 1234567)
    assert print_number(dic, "harry") == "harry=1234567"


def test_return_number_false():
        dic = {}
        dic.setdefault("harry", 1234567)
        assert print_number(dic, "dick") == "Not found"
