def main():
    name = input ("File name :").lower().strip()
    print (output(extension(name)))

def output (extension):
    output = extension.replace(".", "")
    if output in ["gif", "jpg", "jpeg", "png"]:
        if output == "jpg":
            return f"image/jpeg"
        else :
            return f"image/{output}"
    elif output in ["pdf", "zip"]:
        return f"application/{output}"
    elif output.endswith("txt"):
        file, txt = output.split(".")
        return f"{txt}/{file}"
    else :
        return (extension)

def extension(name):
    list = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]
    for i in list:
        if name.endswith(i):
            if i == "txt":
                return name
        else :
            return i
    if not name.endswith(i):
        return "application/octet-stream"


main()
