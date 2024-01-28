import sys
from os.path import splitext
from os import path
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet =ImageOps.fit(img, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_entension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_entension(file2[1]) == False:
        sys.exit("Invalid input")

def check_entension(file):
    if file in [".jpg",".jpeg",".png"]:
        return True
    return False


if __name__=="__main__":
    main()
