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
while True:
    date = input("Date :").strip()
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        new_date = date.replace(", ", " ")
        month, day, year = new_date.split(" ")
        if month in months :
            month = months.index(month) + 1
    elif " " in date and "," not in date :
        month, day, year = date.split(" ")
        True
    try:
        if int(month) > 12 or int(day) > 31 :
            True
        else:
            break
    except ValueError :
        continue
    else :
        True

print (f"{year}-{int(month):02}-{int(day):02}")

