import pytest
from find_availability import availabile_list, day_index, date_object
from find_availability import formated_schedual, company_holiday
from find_availability import find_availabile_work_hours

DATA = {
    "1": {
        "name": "Mark Virtue",
        "availability": [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 4, 4, 4, 0]],
            ["01/01/2016", None, [0, 8, 8, 8, 8, 8, 0]],
        ],
    },
    "2": {
        "name": "Anne Prins",
        "availability": [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 8, 8, 4, 0]],
        ],
    },
}

AVAIL_LIST = [
    ["01/01/2015", "12/31/2015", [0, 4, 4, 4, 4, 4, 0]],
    ["01/01/2016", None, [0, 8, 8, 8, 8, 8, 0]],
]

TABLE1 = [
    (AVAIL_LIST, "12/06/2015", "12/09/2015", ['"12/06/2015",0',
                                              '"12/07/2015",4',
                                              '"12/08/2015",4',
                                              '"12/09/2015",4']),
    (AVAIL_LIST, "01/01/2014", "01/04/2014", ['"01/01/2014",0',
                                              '"01/02/2014",0',
                                              '"01/03/2014",0',
                                              '"01/04/2014",0']),
    (AVAIL_LIST, "12/29/2015", "01/02/2016", ['"12/29/2015",4',
                                              '"12/30/2015",4',
                                              '"12/31/2015",4',
                                              '"01/01/2016",0',  # Holiday
                                              '"01/02/2016",0']),
]

TABLE2 = [
    (date_object("01/11/2017"), 3),
    (date_object("12/06/2015"), 0),
    (date_object("12/05/2015"), 6),
]

TABLE3 = [
    ("01/11/2017", "2017-01-11"),
    ("12/06/2015", "2015-12-06"),
    ("12/05/2015", "2015-12-05"),
    ('12/05/2015', "2015-12-05"),
]

TABLE4 = [
    ('2,"03/16/2016","06/16/2016",[0,8,8,8,8,0,0]\n',
     [0, 1, 1, 1, 1, 1, 0],
     ['03/16/2016', '06/16/2016', [0, 8, 8, 8, 8, 0, 0]]),
    ('3,"01/01/2017",null,null\n',
     [0, 1, 1, 1, 1, 1, 0],
     ['01/01/2017', None, [0, 1, 1, 1, 1, 1, 0]])
]

TABLE5 = [
    (date_object("01/01/2016"), True),
    (date_object("01/02/2016"), False),
]

TABLE6 = [
    (1, "12/06/2015", "12/09/2015", ['"12/06/2015",0',
                                     '"12/07/2015",8',
                                     '"12/08/2015",8',
                                     '"12/09/2015",4']),
    (1, "01/01/2014", "01/04/2014", ['"01/01/2014",0',
                                     '"01/02/2014",0',
                                     '"01/03/2014",0',
                                     '"01/04/2014",0']),
    (1, "12/29/2015", "01/02/2016", ['"12/29/2015",8',
                                     '"12/30/2015",4',
                                     '"12/31/2015",10',
                                     '"01/01/2016",0',  # Holiday
                                     '"01/02/2016",0']),
]


@pytest.mark.parametrize('data, start, stop, result', TABLE1)
def test_available_list(data, start, stop, result):
    """Test that availabile_list returns the correct
       list of availible work hours"""
    assert availabile_list(data, start, stop) == result


@pytest.mark.parametrize('date, index', TABLE2)
def test_day_index(date, index):
    """Test that day_index returns the correct day of the
        week based on the inputed date: "month/day/year", "12/01/2017"
    """
    assert day_index(date) == index


@pytest.mark.parametrize('date, result', TABLE3)
def test_date_object(date, result):
    """Test that date_object returns a valid datetime.date object"""
    date1 = date_object(date)
    assert date1.isoformat() == result


@pytest.mark.parametrize('line, co, result', TABLE4)
def test_formated_schedual_types(line, co, result):
    """Check the types of the returned elements in list"""
    assert isinstance(formated_schedual(line, co)[0], str)
    assert isinstance(formated_schedual(line, co)[2], list)


@pytest.mark.parametrize('line, co, result', TABLE4)
def test_formated_schedual(line, co, result):
    """Check the return value of formated_schedual()"""
    assert formated_schedual(line, co) == result


@pytest.mark.parametrize("date, result", TABLE5)
def test_company_holiday(date, result):
    """Test return value of company_holiday(date):"""
    assert company_holiday(date) == result


@pytest.mark.parametrize("eid, start, stop, result", TABLE6)
def test_find_available_work_hours(eid, start, stop, result):
    """Test find_availabile_work_hours() output"""
    assert find_availabile_work_hours(eid, start, stop) == result
