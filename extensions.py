def main():
    name = input ("File name :")
    ext = extension(name).replace(".", "")
    if ext in ["gif", "jpg", "jpeg", "png"]:
        print (f"image/{ext}")
    elif ext in ["pdf", "txt", "zip"]:
        print (f"application/{ext}")
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
