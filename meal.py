def main():
    question = input ("What time is it?")
    number_hours = convert(question)
    if 7.00 <= number_hours <= 8.00:
        print ("breakfast time")
    elif 12.00 <= number_hours <= 13.00:
        print("lunch time")
    elif 18.00 <= number_hours <= 19.00:
        print ("dinner time")
    else :
        print("")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    number_hours = float(hours) + minutes
    return number_hours


if __name__ == "__main__":
    main()
