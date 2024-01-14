answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer_corrected = answer.lower().strip()
match answer_corrected:
    case "forty two" | "forty-two" | "42" :
        print ("Yes")
    case _:
        print ("No")
