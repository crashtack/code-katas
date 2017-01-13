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


def company_holiday(date):
    """
        Return True if date is a company holiday
        else return False
    """
    holidays = ["01/01/2015", "01/01/2016", "01/01/2017",
                "12/25/2015", "12/25/2016", "12/25/2017"]
    for i in holidays:
        if date_object(i) == date:
            return True

    return False


def availabile_list(avail_list, start, stop):
    """
        Return a list of avalible work hours for the given
        start and stop date based on the passed in data set.

        avail_list format = [
            ["01/01/2015", "12/31/2015", [0, 4, 4, 4, 4, 4, 0]],
            ["01/01/2016", None, [0, 8, 8, 8, 8, 8, 0]],
        ]
    """
    start = date_object(start)
    stop = date_object(stop)
    current = start
    result = []

    while current <= stop:
        found = False

        if company_holiday(current):
            result.append('"{:02d}/{:02d}/{}",0'.format(
                current.month,
                current.day,
                current.year))
        else:
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


def formated_schedual(line, company_hours):
    """
        Parse and return the schedual information
        set the available hours to company_hours if no override is provided
    """
    line = line.rstrip('\n').split(',', maxsplit=3)
    start = line[1].strip("'").strip('"')
    schedual = []

    if line[2] == 'null':
        stop = None
    else:
        stop = line[2].strip("'").strip('"')

    if line[3] == 'null':
        schedual = company_hours
    else:
        temp = line[3].strip("[").strip("]")
        temp = temp.split(',')
        for i in temp:
            schedual.append(int(i))

    return [start, stop, schedual]


def find_availabile_work_hours(employee_id, start, stop):
    """
        Format the input file into a dictionary containing the
        employee availability information and print available
        hours based on input employee_id, start, and stop
        after calling availabile_list() function.

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
    filename = "find_availability.txt"
    employee_data = {}
    company_hours = []
    current = 0
    emp_num = 0

    with open(filename, 'r') as fh:
        all_lines = fh.readlines()

    for index, line in enumerate(all_lines):
        if line.startswith(('\n', '#')):
            pass
        else:
            temp = line.split(',')
            current = index
            for i in temp:
                company_hours.append(int(i.rstrip('\n')))
            break

    for line in all_lines[current + 1:]:
        if line.startswith(('\n', '#')):
            continue
        else:
            temp = line.split(',', maxsplit=4)
            if int(temp[0]) > emp_num:
                employee_data[temp[0]] = {"name": temp[1], "availability": []}
                emp_num += 1
            else:
                if len(temp) > 3:
                    employee_data[temp[0]]["availability"] \
                        .append(formated_schedual(line, company_hours))

    employee_id = str(employee_id)
    avail = employee_data[employee_id]["availability"]

    output = []
    for i in availabile_list(avail, start, stop):
        print(i)
        output.append(i)     # building output list for testablility

    return output


if __name__ == "__main__":
    find_availabile_work_hours(1, "12/06/2015", "12/09/2015")
