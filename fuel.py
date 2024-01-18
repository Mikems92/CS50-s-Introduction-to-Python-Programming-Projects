while True :
    num = input("Fraction: ")
    index = num.find("/")
    try:
        x = int(num[:index])
        y = int(num[index+1:])
        fraction = int(x*100/y)
        if x > y :
            continue
    except (ValueError, ZeroDivisionError):
        continue
    else:
        break
if fraction >= 99:
    print ("F")
elif fraction <= 1:
    print ("E")
else:
    print(f"{fraction}%")
