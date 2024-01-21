import inflect


p = inflect.engine()
list_names =[]
while True:
    try:
        names = input("Name: ")
        list_names.append(names)
    except EOFError:
        print ("")
        break
if len(list_names) < 3:
    print("Adieu, adieu, to", p.join((list_names), final_sep= ""))
else:
    print("Adieu, adieu, to", p.join((list_names)))
