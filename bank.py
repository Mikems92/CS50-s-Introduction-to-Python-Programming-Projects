greeting = input ("Greeting: ")
greetings = greeting.strip().lower()
if greetings.startswith("hello"):
    print ("$0")
elif greetings.startswith("h") and not greetings.startswith("hello"):
    print ("$20")
else :
    print ("$100")
