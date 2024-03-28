import random
from inputimeout import inputimeout, TimeoutOccurred


def main():
    print (quizz())

def quizz():
    #Initializing the iteration variable to use in while loop
    i = 0
    #Initializing the score
    s = 0
    #Initializing the input
    r = 21
    while i < 10:
        #Program to give a value (integer between 0 and 10 both included) to x and y randomly
        x = random.randint (0, 10)
        y = random.randint (0, 10)
        resultat = int(x + y)
        #Printing the (i+1)th operation and difficulty level
        print(f"{i+1}- {difficulty (resultat)}")
        #Printing the operation
        print (f"   {x} + {y} = " , end="")
        try:
            #Program requesting answer. User has a limited time to answer depending operation difficulty level
            r = int(inputimeout(prompt="", timeout= timer(difficulty(resultat))))
        except (TimeoutOccurred, ValueError) :
            pass
        #If good answer, incrementing score and printing good answer
        if r == resultat:
            s = s + 1
            print("Good answer 👍🙂")
        #If bad answer, printing bad answer
        else:
            print("Bad answer 👎🙁")
        i += 1
    #Return final score at the end in %
    return score(s)


def difficulty (d):
    if d <= 5:
        return f"Level : Easy"
    elif d <= 12:
        return f"Level : Medium"
    else:
        return f"Level : Hard"


def timer (t):
    match t:
        case "Level : Easy":
            #If operation difficulty level is easy, user has 5s maximum to answer
            return 5
        case "Level : Medium":
            #If operation difficulty level is medium, user has 7s maximum to answer
            return 7
        case "Level : Hard":
            #If operation difficulty level is easy, user has 10s maximum to answer
            return 10


def score (s):
    #s for final score
    if s <= 5:
        return f"Your score is {s*10}%, Not enough 👎🙁"
    elif s <= 7:
        return f"Your score is {s*10}%, Good job 👍"
    else:
        return f"Your score is {s*10}%, Excellent 👍🙂"


if __name__=="__main__":
    main()
