def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum() :
            for i in s:
                if i.isdigit():
                    c = s.index(i)
                    if int(i) != 0 and s[c:].isdigit():
                        return True
                    else:
                        return False
                




main()
