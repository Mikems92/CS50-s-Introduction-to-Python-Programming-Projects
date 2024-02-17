expression = input("Expression :")
x, y, z = expression.split(" ")

if y == "+":
    e = int(x) + int(z)
    print (f"{e:.1f}")
elif y == "-":
    e = int(x) - int(z)
    print (f"{e:.1f}")
elif y == "*":
    e = int(x) * int(z)
    print (f"{e:.1f}")
elif y == "/":
    if z == "0":
        print ("Impossible")
    else:
        e = int(x) / int(z)
        print (f"{e:.1f}")
