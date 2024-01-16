amount_due = int(50)
print ("Amount Due:", amount_due)
while amount_due != 0 :
    insert_coin = int(input("Insert Coin :"))
    if insert_coin == 5 :
        amount_due = amount_due - insert_coin
        if amount_due == 0 :
            print("Change Owed:", amount_due)
        else :
             print ("Amount Due:", amount_due)
    elif insert_coin == 10 :
        if insert_coin > amount_due :
            print("Change Owed:", insert_coin - amount_due)
            amount_due = 0
        else :
            amount_due = amount_due - insert_coin
            if amount_due == 0 :
                print("Change Owed:", amount_due)
            else :
                print ("Amount Due:", amount_due)
    elif insert_coin == 25 :
        if insert_coin > amount_due :
            print("Change Owed:", insert_coin - amount_due)
            amount_due = 0
        else :
            amount_due = amount_due - insert_coin
            if amount_due == 0 :
                print("Change Owed:", amount_due)
            else :
                print ("Amount Due:", amount_due)
    else :
        print ("Amount Due:", amount_due)

