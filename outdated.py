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
    date = input ("Date: ").strip()
    if "/" in date:
        mm, dd, yyyy = date.split("/")
    elif " " in date and "," in date :
        new_date = date.replace(",", "")
        mm, dd, yyyy = date.split(" ")
        if mm in months:
            mm = int(months.index(mm)) + 1
    elif " " in date and "," not in date :
        mm, dd, yyyy = date.split(" ")
        True

    try:
        if int(mm) > 12 or int(dd) > 31 :
            True
        else:
            break
    except ValueError:
        continue
    else:
        True

print (f"{yyyy}-{int(mm):02}-{int(dd):02}")

