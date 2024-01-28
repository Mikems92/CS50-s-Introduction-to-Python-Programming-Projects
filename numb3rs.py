import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   if re.search(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip.strip()) :
        first, sec, third, fourth = ip.split(".")
        if 0 <= int(first) <= 255 and 0 <= int(sec) <= 255 and 0 <= int(third) <= 255 and 0 <= int(fourth) <= 255:
            return True
        else :
            return False
    else:
        return False


if __name__ == "__main__":
    main()
