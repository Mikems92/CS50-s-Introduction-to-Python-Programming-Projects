fraction = input("Fraction: ").strip()
x, y = fraction.split("/")

try:
    ratio = int(x)*100/int(y)
    resultat = round (ratio)
    if resultat <= 1:
        print ("E")
    elif resultat >= 99:
        print ("F")
    else :
        print (f"{resultat}%")
except (ValueError, ZeroDivisionError):
    ...
