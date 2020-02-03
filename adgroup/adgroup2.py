import sys
import json
import datetime

"""
USAGE:

In terminal run script without argument to get a string-list of names that have namedays today.
In terminal run script with argument (name in genitive form, e.g. Joanny, Błażeja) to get a string-list of date when 
current name has a namedays.
"""


class NameDays:
    def __init__(self, name=None):
        self.name = name
        self._json_file = self.load_file('imieniny.json')

    @staticmethod
    def load_file(file):
        """
        Loads json file
        :param file: json file
        :return: json object
        """
        try:
            with open(file, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            return 'File cannot be found.'

    def search_nameday_by_name(self) -> str:
        """
        Gives a string-list of dates when given name has namedays
        :return: str
        """

        if not self.name.isalpha():
            return 'Name must be a string.'

        namedays_list = []

        for row in self._json_file.keys():
            if self.name in self._json_file[row]:
                namedays_list.append(row)

        if namedays_list:
            return ", ".join(namedays_list)
        else:
            return 'Entered value cannot be found. Try genitive form of a name.'

    def search_nameday_by_today(self):
        """
        Gives a string-list of name that have namedays today
        :return: str
        """
        date = datetime.datetime.today().strftime('%d-%m')
        return ", ".join(self._json_file[date])

    def search_nameday_by_date(self, date):
        if date[2] == '-':
            return ", ".join(self._json_file[date])
        else:
            return 'Incorrect date format. Please use dd-mm.'

    def __str__(self):
        if self.name is not None:
            return self.search_nameday_by_name()
        else:
            return self.search_nameday_by_today()


if __name__ == '__main__':
    try:
        app = NameDays(name=sys.argv[1])
    except IndexError:
        app = NameDays(name=None)
    finally:
        print(app)
