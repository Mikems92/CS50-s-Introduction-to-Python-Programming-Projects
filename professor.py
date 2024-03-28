import random


def main():
    level = get_level()
    problems = 10
    score = 0
    tries = 3
    while problems != 0:
        if tries == 3 :
            x, y = generate_integer(level)
        try:
            answer = int(input(f"{x} + {y} = "))
            problem = x + y
            if answer == problem :
                problems -= 1
                score += 1
                tries = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            tries -= 1
            pass
        if tries == 0 :
            print((f"{x} + {y} = {x + y}"))
            tries = 3
            problems -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    match level:
        case "f{1}" :
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case "f{2}" :
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case "f{3}" :
            x = random.randint(100, 999)
            y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
