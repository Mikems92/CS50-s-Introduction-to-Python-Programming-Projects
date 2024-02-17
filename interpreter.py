expression = input("Expression :")
x, y, z = expression.split(" ")

match y:
    case "+":
        e = int(x) + int(z)
        print (f"{e:.1f}")
    case "-":
        e = int(x) - int(z)
        print (f"{e:.1f}")
    case "*":
        e = int(x) * int(z)
        print (f"{e:.1f}")
    case "/":
        if z == "0":
            print ("Impossible")
        else:
            e = int(x) / int(z)
            print (f"{e:.1f}")
