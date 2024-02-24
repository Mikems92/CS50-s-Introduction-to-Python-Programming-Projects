list = []
dict = {}
while True:
    try:
        item = input().upper()
        list.append(item)
    except EOFError:
        for i in list:
            dict[i] = list.count(i)
        break
print ("")

for j in sorted(dict.keys()):
    print (f"{dict[j]} {j}")
