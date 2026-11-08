cost = 50
while cost != 0:
    print("Amount Due:", cost)
    insert = int(input("Insert Coin: "))
    if (insert == 5) or (insert == 10) or (insert == 25):
        cost -= insert