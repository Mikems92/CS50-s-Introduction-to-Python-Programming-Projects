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
for i in fruit:
    j = fruit.count(i)
    dic [i] = j
for k in sorted(dic.keys()):
    print(dic[k], k)
