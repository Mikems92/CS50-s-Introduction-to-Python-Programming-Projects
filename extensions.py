def main():
    name = input ("File name :").lower().strip()
    print (ext(extension(name)))


def ext(extension)
    ext = extension.replace(".", "")
    if ext in ["gif", "jpg", "jpeg", "png"]:
        if ext == jpg :
            return f"image/jpeg"
        else :
            return f"image/{ext}"
    elif ext in ["pdf", "txt", "zip"]:
        return f"application/{ext}"
    else :
        return extension(name)

def extension(name):
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    for i in list:
        if name.endswith(i):
            return i
    if not name.endswith(i):
        return "application/octet-stream"


main()
