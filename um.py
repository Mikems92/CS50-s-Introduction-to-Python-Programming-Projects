import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r'\bum\b'
    match = re.findall (regex, s.lower())
    return len(match)


if __name__ == "__main__":
    main()
