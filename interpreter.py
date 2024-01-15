x, y, z = input("Expression : ").split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "/":
    print(float(x) / float(z))
elif z == "*":
    print(float(x) * float(z))
