input = input ("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
output = ""
for i in input :
    if i not in vowels :
         output = output + i
print ("Output: ", output)
