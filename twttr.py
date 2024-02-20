input = input ("Input: ")
list = []

for i in input:
    if i not in ["A", "a", "E", "e", "I", "i", "o", "O", "u", "U"]:
        list.append(i)
print ("Output: ", end="")

for j in list:
    print (j, end="")
print("")


