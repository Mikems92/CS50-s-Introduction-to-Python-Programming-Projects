amount_due = int(50)
print (f"Amount Due:{amount_due}")
while amount_due > 0 :
    insert_coin = int(input("Insert Coin:"))
    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5 :
        amount_due -= insert_coin
        if amount_due <= 0:
            print (f"Change Owed:{amount_due * (-1)}")
        elif amount_due > 0 :
            print (f"Amount Due:{amount_due}")
    else:
        True




