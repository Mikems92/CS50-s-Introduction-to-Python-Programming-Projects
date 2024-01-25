import sys
from os import path


if len(sys.argv) > 2:
    sys.exit("Too many arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif sys.argv[1].endswith(" .py") :
    sys.exit
else :
    pass

count = 0
if sys.argv[1].endswith(".py") :
    if path.exists(sys.argv[1]):
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") or line.lstrip() == "":
                    pass
                else:
                    count += 1
            print(count)
    else :
        print ("File does not exist")
else :
    print ("Not a Python file")




