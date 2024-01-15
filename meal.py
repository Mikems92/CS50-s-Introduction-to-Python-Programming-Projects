def main():
    time_to_eat = convert(input("What time is it ? "))
    print(time_to_eat)


def convert(time):
    hours , minutes = time.split (":")
    x = int(hours) + int(minutes)/60

    if 7 <= x <= 8 :
        return "It's breakfast time"
    elif 12 <= x <= 13 :
        return "It's lunch time"
    elif 18 <= x <= 19 :
        return "It's dinner time"
    else :
        return ""


if __name__ == "__main__":
    main()
