list = []
dict = {}
while True:
    try:
        item = input().upper()
        list.append(item)
        list.sort()
    except EOFError:
        for i in list:
            dict[i] = list.count(i)
        break
print ("")

for j in dict:
    print (f"{dict[j]} {j}")
