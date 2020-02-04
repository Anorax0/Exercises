import sys
import json
import datetime

"""
USAGE:

In terminal run script without argument to get a string-list of names that have namedays today.
In terminal run script with argument (name in genitive form, e.g. Joanny, Błażeja) to get a string-list of date when 
current name has a namedays.
"""


def open_file(file: str):
    """
    Json file handler
    :type file: str
    :return json file
    """
    try:
        with open(file, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return 'File cannot be found.'


def main(name: str = None):
    """
    Searches for namedays for entered name, if name is not entered, returns namedays for today
    :param name: str
    :return: str
    """

    file = open_file('imieniny.json')

    if name:
        if not name.isalpha():
            return 'Name must be a string.'

        namedays_list = []

        for row in file.keys():
            if name in file[row]:
                namedays_list.append(row)

        if namedays_list:
            return ", ".join(namedays_list)
        else:
            return 'Entered value cannot be found. Try genitive form of a name.'

    else:
        date = datetime.datetime.today().strftime('%d-%m')
        return ", ".join(file[date])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(main(name=sys.argv[1]))
    else:
        print(main(name=None))
