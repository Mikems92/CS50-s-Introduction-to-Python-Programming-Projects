def main():
    name = input ("File name :").lower().strip()
    print (output(extension(name), name))

def output (extension, name):
    if extension.endswith(("gif", "jpg", "jpeg", "png")):
        if extension.endswith == "jpg":
            return f"image/jpeg"
        else :
            return f"image/{extension}"
    elif extension.endswith(("pdf", "zip")):
        return f"application/{extension}"
    elif extension.endswith("txt"):
        file, _ = name.split(".txt")
        return f"text/{file}"
    else :
        return (extension)

def extension(name):
    if name.endswith(("gif", "jpg", "jpeg", "png", "pdf", "txt", "zip")):
        _, ext = name.split(".")
        return ext
    else :
        return "application/octet-stream"


main()
