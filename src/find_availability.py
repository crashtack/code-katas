"""
    Find Availability Problem

    Given:
        A list of standard company work hours [0, 8, 8, 8, 8, 8, 0]
        where the first '0' is Sunday and the last '0' is Saturday.

        A list of employees with an 'id', 'name', and optional employee-
        specific weekly hours overrides.
            [
                { 1, "01/01/2015", "12/31/2015"}, [0,4,4,8,8,4,0]},
                { 1, "01/01/2016", null}, [0,8,8,8,8,0,0]}
            ]

    Implement a 'find_availabile_work_hours(user_id, from, to)' function
    that outputs availability in the format:
        "12/06/2015",0
        "12/07/2015",4
        "12/08/2015",4
        "12/09/2015",8

    The program calling the 'find_availabile_work_hours()' function takes
    in data in the folling format:
        # example input for the find availability problem

        # company work hours
        0,8,8,8,8,8,0

        # employees
        1,Mark Virtue
        2,Anne Prins

        # mark's availability
        1,"01/01/2015","12/31/2015",[0,8,8,4,10,10,0]
        1,"01/01/2016",null,[0,8,8,8,8,8,0]

        # anne's availability
        2,"03/16/2016","06/16/2016",[0,8,8,8,8,0,0]

        # find availability for user and dates
        1,"12/16/2015","01/15/2016"
"""
import calendar
import datetime


def day_index(date):
    """
        Returns the day of the week index given a datetime.date object
        based on Sunday = index 0
    """
    month = date.month
    day = date.day
    year = date.year

    index = calendar.weekday(year, month, day)
    return (index + 1) % 7


def date_object(date):
    """
        Returns a datetime.date() object based on the inputed date string
    """
    date_list = date.split('/')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])

    return datetime.date(year, month, day)


def availabile_list(avail_list, start, stop):
    """
        Return a list of avalible work hours for the given
        start and stop date based on the passed in data set.

        avail_list format = [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 4, 4, 4, 0]],
            ["01/01/2016", None, [0, 8, 8, 8, 8, 8, 0]],
        ]
        TODO: Check for company holiday
    """
    start = date_object(start)
    stop = date_object(stop)
    current = start
    result = []

    while current <= stop:
        found = False

        for element in avail_list:
            emp_start = date_object(element[0])

            # Handling the None end date in avail_list
            if element[1]:
                emp_stop = date_object(element[1])
            else:
                emp_stop = stop

            if emp_start <= current and emp_stop >= current:
                result.append('"{:02d}/{:02d}/{}",{}'.format(
                    current.month,
                    current.day,
                    current.year,
                    element[2][day_index(current)]))
                found = True

        if found is False:
                result.append('"{:02d}/{:02d}/{}",0'.format(
                    current.month,
                    current.day,
                    current.year))

        current += datetime.timedelta(days=1)

    return result


def find_available_work_hours(employee_id, start, stop):
    """
        Format the input file into a dictionary containing the
        employee availibility information and print availible
        hours based on input employee_id, start, and stop
        date after calling availabile_list() function.

        data format:
            {
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
    """
    pass
