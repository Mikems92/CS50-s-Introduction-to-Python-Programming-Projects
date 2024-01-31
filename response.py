import re


def main():
    print (response(input("What's your email address :")))


def response (s):
    if match := re.search(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", s):
        return "Valid"
    else :
        return "Invalid"


if __name__ == "__main__":
    main()
