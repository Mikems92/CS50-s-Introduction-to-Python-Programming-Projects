import random

while True:
    n = input ("level : ")
    if n.isdigit() and int(n) <= 0:
        True
    elif n.isdigit() and int(n) > 0:
        break
    else :
        True
random_num = random.randint(1, int(n))
while True:
    guess = input ("Guess : ")
    if not guess.isdigit () :
        True
    elif guess.isdigit () :
        if int(guess) > random_num :
            print ("Too large!")
            True
        elif int(guess) < random_num :
            print ("Too small!")
            True
        else:
            print ("Just right!")
            break



