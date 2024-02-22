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
            for i in s:
                if i.isnumeric():
                    c = s.index(i)
                    if s[c] != 0 and s[c:].isnumeric():
                        return True
                elif i.isalpha():
                    return True




main()
