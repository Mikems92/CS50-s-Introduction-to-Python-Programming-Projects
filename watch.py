import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if output := re.search (r'^(.*)http(s)?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)"(.*)$', s):
        return("https://youtu.be/" + output.group(4))
    return(f"None")


if __name__ == "__main__":
    main()
