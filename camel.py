camelcase = input ("camelCase: ")
list = list()

for i in camelcase:
    if i.islower():
        list.append(i)
    elif i.isupper():
        list.append("_")
        list.append(i.lower())

for j in list:
    print (j, end="")
    
print("")

