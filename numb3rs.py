import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]{1,3}\.){3}[0-9]{1,3}$", ip.strip()) :
        bytes = ip.split(".")
        for byte in bytes:
            if int(byte) < 0 or int(byte) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
