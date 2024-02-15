def main():
    name = input ("File name :")
    print (extension(name))


def extension(name):
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    for i in list:
        if name.endswith(i):
            return i
    if not name.endswith(i):
        return "application/octet-stream"


main()
