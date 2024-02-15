def main():
    name = input ("File name :").lower().strip()
    print (output(extension(name), name))

def output (extension, name):
    output = extension.replace(".", "")
    if output in ["gif", "jpg", "jpeg", "png"]:
        if output == "jpg":
            return f"image/jpeg"
        else :
            return f"image/{output}"
    elif output in ["pdf", "zip"]:
        return f"application/{output}"
    elif extension.endswith("txt"):
        file, txt = name.split(".txt")
        return f"text/{file}"
    else :
        return (extension)

def extension(name):
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    for i in list:
        if name.endswith(i):
            return i
    if not name.endswith(i):
        return "application/octet-stream"


main()
