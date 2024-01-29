import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    output = re.search (r'^.*https?://www\.youtube\.com/embed/([a-zA-Z0-9]+).+$', s)
    if output :
        return(f"https://youtu.be/{output.group(1)}")
    else :
        return(f"None")


if __name__ == "__main__":
    main()
