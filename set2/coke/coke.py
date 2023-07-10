coke = 50

while coke > 0:
    print("Amount Due: ", coke)
    invoer = int(input("Insert Coin: "))
    if invoer == 5 or invoer == 10 or invoer == 25:
        coke = coke - invoer


print("Change Owed: ", coke * -1)





