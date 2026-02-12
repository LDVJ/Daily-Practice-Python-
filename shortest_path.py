def find_closer_beach(x):
    diff_rk_beach = x - 1
    diff_ru_beach = 49 - x

    if diff_rk_beach > diff_ru_beach:
        print("RU Beach")
    elif diff_rk_beach < diff_ru_beach:
        print("RK Beach")
    else:
        print("Go Anywhere!")


x = int(input("Enter you coordinate: "))
find_closer_beach(x=x)