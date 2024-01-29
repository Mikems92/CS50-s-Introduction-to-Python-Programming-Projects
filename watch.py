import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    output = re.search (r'^.*https?://www\.youtube\.com/embed/([^"]+)".+$', s)
    if output :
        return(f"https://youtu.be/{output.group(1)}")
    else :
        return(f"None")


if __name__ == "__main__":
    main()
