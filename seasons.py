from datetime import datetime, date
import inflect
import sys
import re

def main():
    date = check_format(input ("Date of Birth: "))
    date_of_birth = convert(age(datetime.strptime(date,"%Y-%m-%d").date()))
    print (f"{date_of_birth} minutes")


def check_format (f):
    if format := re.match(r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$", f) :
        return f"{f}"
    else:
        sys.exit ("Invalid date")


def age(a):
    now = date.today()
    return f"{now - a}"


def convert(c):
    p = inflect.engine()
    date, time = c.split("days, ")
    words = p.number_to_words(int(date) * 24 * 60)
    return words


if __name__ == "__main__":
    main()
