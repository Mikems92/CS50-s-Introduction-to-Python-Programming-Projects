def main():
    y = convert(input("What time is it ? "))
    if 7 <= y <= 8 :
        print("breakfast time")
    elif 12 <= y <= 13 :
        print("lunch time")
    elif 18 <= y <= 19 :
        print("dinner time")
    else :
        print("")


def convert(time):
    hours , minutes = time.split (":")
    x = int(hours) + int(minutes)/60
    return x


if __name__ == "__main__":
    main()
