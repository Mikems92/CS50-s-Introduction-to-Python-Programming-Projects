fruit = []
count = []
dic = {}
while True :
    try:
        item = input("").upper()
        fruit.append(item)
        True
    except EOFError :
        print ("\n")
        break
for k in sorted(dic.keys()):
    for i in fruit:
        dic [i] = fruit.count(i)
print(dic[k], k)
