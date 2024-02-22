while True:
    fraction = input("Fraction: ").strip()
    try:
        x, y = fraction.split("/")
        ratio = int(x)*100/int(y)
        resultat = round (ratio)
        if resultat <= 1:
            print ("E")
            break
        elif 99 <= resultat <= 100:
            print ("F")
            break
        elif 100 <= resultat :
            continue
        else :
            print (f"{resultat}%")
            break
    except (ValueError, ZeroDivisionError):
        continue
