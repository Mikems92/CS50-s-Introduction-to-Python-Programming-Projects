months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
]
while True :
    date = input ("Date: ")
    if "/" in date:
        mm, dd, yyyy = date.split("/")
    elif " " in date:
        mm, dd, yyyy = date.split(" ")
        if mm in months:
            mm = int(months.index(mm)) + 1
            if "," in dd:
                dd = dd.replace(",", "")
    try:
        if int(mm) > 12 and int(dd) > 31 :
            True
        else:
            break
    except ValueError:
        continue
    else:
        False

print (f"{yyyy}-{int(mm):02}-{int(dd):02}")

