import random

while True:
    n = int(input ("level : "))
    if n <= 0 :
        True
    else:
        break
random_num = random.randint(1, n)
while True:
    guess = int(input ("Guess : "))
    if random_num <= 0:
        True
    elif random_num >= 0:
        if guess > random_num :
            print ("Too large")
            True
        elif guess < random_num :
            print ("Too small")
            True
        else:
            print ("Just right")
            break



