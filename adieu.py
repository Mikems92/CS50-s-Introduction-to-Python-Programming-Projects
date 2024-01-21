import inflect


p = inflect.engine()
list_names =[]
while True:
    try:
        names = input("Name: ")
        list_names.append(names)
    except EOFError:
        print ("\n")
        break
print("Adieu, adieu, to ", p.join((list_names), final_sep= ""))
