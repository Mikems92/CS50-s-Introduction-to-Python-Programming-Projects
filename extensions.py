def main():
    name = input ("File name :")
    if extension(name) in [".gif", ".jpg", ".jpeg", ".png"]:
        print (f"image/{extension(name)}")
    elif extension(name) in [".pdf", ".txt", ".zip"]:
        print (f"application/{extension(name)}")
    else :
        print (extension(name))

def extension(name):
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    for i in list:
        if name.endswith(i):
            return i
    if not name.endswith(i):
        return "application/octet-stream"


main()
