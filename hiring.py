def check_hiring(n, salaries, k):
    expected = 0
    for amount in salaries:
        expected += amount
    
    if expected <= k:
        print("Hire")
    else:
        print("No Hire")