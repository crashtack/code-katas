import pytest
from find_availablity import return_availabile, day_index

DATA = {
    "1": {
        "name": "Mark Virtue",
        "avalability": [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 8, 8, 4, 0]],
            ["01/01/2016", None, [0, 8, 8, 8, 0, 0]],
        ],
    },
    "2": {
        "name": "Anne Prins",
        "avalability": [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 8, 8, 4, 0]],
        ],
    },
}


TABLE1 = [
    (DATA, 1, "12/116/2015", "01/15/2016", [["12/06/2015", 0],
                                            ["12/07/2015", 4],
                                            ["12/08/2015", 4],
                                            ["12/09/2015", 8]]),
]

TABLE2 = [
    ("01/11/2017", 3),
    ("12/06/2015", 0),
    ("12/05/2015", 6),
]


# @pytest.mark.parametrize('data, employee, start, stop, result', TABLE1)
# def test_return_available(data, employee, start, stop, result):
#     """Test that return_availabile returns the correct
#        list of availible work hours"""
#     hours = [0, 8, 8, 8, 8, 8, 0]
#     assert return_availabile(data, hours, employee, start, stop) == result


@pytest.mark.parametrize('date, index', TABLE2)
def test_day_index(date, index):
    """Test that day_index returns the correct day of the
        week based on the inputed date: "month/day/year", "12/01/2017"
    """
    assert day_index(date) == index
