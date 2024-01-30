import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search (r"^([0-9]+):*[ ]*([0-9]*) ([A-Z]+) to ([0-9]+):*[ ]*([0-9]*) ([A-Z]+)$", s) :
        group1 = int(time.group(1))
        meridiem1 = time.group(3)
        group4 = int(time.group(4))
        meridiem2 = time.group(6)
        if group1 < 12 and group4 < 12:
            return h_less_12(group1, time.group(2), group4, time.group(5), meridiem1, meridiem2)
        elif group1 == 12 and group4 == 12:
            return h_equals_12(group1, time.group(2), group4, time.group(5), meridiem1, meridiem2)
    else:
        raise ValueError


def h_less_12(grp1, grp2, grp4, grp5, m1, m2):
    if grp2 and grp5:
        grp2 = int(grp2)
        grp5 = int(grp5)
        if grp2<60 and grp5<60:
            if m1 == "PM":
                grp1 += 12
                return f"{'{:02d}'.format(grp1)}:{'{:02d}'.format(grp2)} to {'{:02d}'.format(grp4)}:{'{:02d}'.format(grp5)}"
            if m2 == "PM":
                grp4 += 12
                return f"{'{:02d}'.format(grp1)}:{'{:02d}'.format(grp2)} to {'{:02d}'.format(grp4)}:{'{:02d}'.format(grp5)}"
    else:
        if m1 == "PM":
            grp1 += 12
            return f"{'{:02d}'.format(grp1)}:00 to {'{:02d}'.format(grp4)}:00"
        if m2 == "PM":
            grp4 += 12
            return f"{'{:02d}'.format(grp1)}:00 to {'{:02d}'.format(grp4)}:00"


def h_equals_12 (grp1, grp2, grp4, grp5, m1, m2):
    if grp2 and grp5:
        grp2 = int(grp2)
        grp5 = int(grp5)
        if m1 == "AM":
            return f"00:{'{:02d}'.format(grp2)} to {'{:02d}'.format(grp4)}:{'{:02d}'.format(grp5)}"
        elif m2 == "AM":
            return f"{'{:02d}'.format(grp1)}:{'{:02d}'.format(grp2)} to 00:{'{:02d}'.format(grp5)}"
    else:
        if m1 == "AM":
            return f"00:00 to {'{:02d}'.format(grp4)}:00"
        elif m1 == "PM":
            return f"{'{:02d}'.format(grp1)}:00 to 00:00"


if __name__ == "__main__":
    main()
