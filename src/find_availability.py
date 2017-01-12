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
        Returns the day of the week index given a data ("12/31/2017")
        based on Sunday = index 0
    """
    date_list = date.split('/')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])

    index = calendar.weekday(year, month, day)

    index = (index + 1) % 7
    return index


def date_object(date):
    """
        Returns a datetime.date() object based on the inputed date string
    """
    date_list = date.split('/')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])

    return datetime.date(year, month, day)


def return_availabile(data, hours, employee, start, stop):
    """
        Return a list of avalible work hours for the given the
        start and stop date based on the passed in data set
        and standard hours.

        data format:
            {
                "1": {
                    "name": "Mark Virtue",
                    "availability": [
                        ["01/01/2015", "12/31/2015", [0, 4, 4, 8, 8, 4, 0]],
                        ["01/01/2016", None, [0, 8, 8, 8, 0, 0]],
                    ],
                },
                "2": {
                    "name": "Anne Prins",
                    "availability": [
                        ["01/01/2015", "12/31/2015", [0, 4, 4, 8, 8, 4, 0]],
                    ],
                },
            }

        hour format: [0, 8, 8, 8, 8, 8, 0]
    """
    start = date_object(start)
    stop = date_object(stop)

    availability = data[employee]["availability"]
    print(availability)
