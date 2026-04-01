try:
    value  =  [int(x) for x in input("Enter you list of numeric vlues with spaces: ").split(" ")]

    max_num = value[0]

    for item in value:
        if item > max_num:
            max_num = item

    print(max_num)
except ValueError:
    print([])
    print("Invalid Value")