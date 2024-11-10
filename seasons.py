import re
import sys
from datetime import date
import inflect

# Initialize inflect
p = inflect.engine()


def main():

    birth_date = input("Date of Birth: ")
    if Birthday.check_date(birth_date) == True:
        minutes_lived = Birthday.minutes(Birthday.year, Birthday.month, Birthday.day)
        # Transform total minutes to words using the function number_to_words from inflect, remove and word and capitalize the string
        minutes_lived_str = p.number_to_words(minutes_lived, andword="").capitalize()
        print(f"{minutes_lived_str} minutes")

    else:
        sys.exit("Invalid date")


# Simple class to store variables for a birth date
class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # A method for check the format of the date
    def check_date(date):
        # Pattern for a valid date format: YYYY-MM-DD
        pattern = r"^(?P<date_year>\d{4})\-(?P<date_month>0[1-9]|1[0-2])\-(?P<date_day>0[1-9]|[12][0-9]|3[01])$"

        if date_match := re.search(pattern, date):
            Birthday.year = int(date_match.group("date_year"))
            Birthday.month = int(date_match.group("date_month"))
            Birthday.day = int(date_match.group("date_day"))

            return True

        else:
            sys.exit("Invalid date")

    # A method that trasnforms the birth date from days to minutes
    def minutes(year, month, day):
        birthday = date(year, month, day)
        current_date = date.today()
        # Diference between current day and birth date to get the days
        difference = current_date - birthday
        # Multiply the difference per hours and minutes (24 * 60)
        return difference.days * 1440


if __name__ == "__main__":
    main()
