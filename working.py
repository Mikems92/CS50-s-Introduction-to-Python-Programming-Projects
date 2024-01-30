import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try :
        if time := re.search (r"^([0-9]+):*[ ]*([0-9]*) ([A-Z]+) to ([0-9]+):*[ ]*([0-9]*) ([A-Z]+)$", s) :
            group1 = int(time.group(1))
            meridiem1 = time.group(3)
            group4 = int(time.group(4))
            meridiem2 = time.group(6)
            if group1<=12 and group4<=12:
                if time.group(2) and time.group(5):
                    group2 = int(time.group(2))
                    group5 = int(time.group(5))
                    if group2<60 and group5<60:
                        if meridiem1 == "PM":
                            group1 += 12
                            return f"{'{:02d}'.format(group1)}:{'{:02d}'.format(group2)} to {'{:02d}'.format(group4)}:{'{:02d}'.format(group5)}"
                        if meridiem2 == "PM":
                            group4 += 12
                            return f"{'{:02d}'.format(group1)}:{'{:02d}'.format(group2)} to {'{:02d}'.format(group4)}:{'{:02d}'.format(group5)}"
                else:
                    if meridiem1 == "PM":
                        group1 += 12
                        return f"{'{:02d}'.format(group1)}:00 to {'{:02d}'.format(group4)}:00"
                    if meridiem2 == "PM":
                        group4 += 12
                        return f"{'{:02d}'.format(group1)}:00 to {'{:02d}'.format(group4)}:00"
    except ValueError:
        return("ValueError")

if __name__ == "__main__":
    main()
