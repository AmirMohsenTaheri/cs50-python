from datetime import date
import inflect
import sys
import operator
import re

p = inflect.engine()

def main():
    today_time = date.today()
    birth =  input("Date of Birth: ")
    if re.search(r"^[0-9]{1,4}\-(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1])$", birth):
        difference = operator.sub(today_time, date.fromisoformat(birth))
        print(convert(difference.days))
    else:
        sys.exit("Invalid date")


def convert(time):
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword="")).capitalize()} minutes"


if __name__ == "__main__":
    main()
