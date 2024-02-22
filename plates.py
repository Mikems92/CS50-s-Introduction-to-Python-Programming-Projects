def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum() :
        if len(s) == 2:
            return True
        elif len(s) > 2:
            if s[2:].isnumeric():
                if s[2] != 0:
                    return True
            elif s[2:].isalpha():
                return True





main()
