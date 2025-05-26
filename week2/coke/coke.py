ao = 50
while ao > 0:
    print("Amount Due:", ao)
    ic = int(input("Insert coin: "))
    if ic == 25 or ic == 10 or ic == 5:
        ao = ao - ic
print("Change Owed:", abs(ao))
