def main():
    name = input ("File name :").lower().strip()


def output (extension):
    output = extension.replace(".", "")
    if output in ["gif", "jpg", "jpeg", "png"]:
        if output == "jpg":
            print (f"image/jpeg")
        else :
            print (f"image/{output}")
    elif output in ["pdf", "zip"]:
        print (f"application/{output}")
    elif output.endswith("txt"):
        file, txt = output.split(".")
        print (f"{txt}/{file}")
    else :
        print (extension)

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
