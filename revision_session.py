def find_closer_beach(x: int) ->str:
    rk = 1
    ru = 49

    if x - rk > ru -x:
        print("RU Beach")
    elif x - rk < ru - x:
        print("RK Beach")
    else:
        print("Go Anywhere")

find_closer_beach(5)