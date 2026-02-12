def choose_chocolate(n, m):
    dairy_milk_amount = 5 * m
    dairy_shots_amount = 2 * m
    dairy_eclairs_amount = 1 * m

    if dairy_milk_amount <= n:
        print("Dairy Milk")
    elif dairy_shots_amount <= n:
        print("Shots")
    elif dairy_eclairs_amount <= n:
        print("Eclairs")
    else:
        print("No Chocolates")


n = int(input("Amount: "))
m = int(input("Students: "))

choose_chocolate(n=n, m=m)