try:
    num_list = [int(x) for x in input("Enter numbers with space: ").split()]

    count = 0

    for num in num_list:
        if num % 2 == 0:
            count += 1

    print(count)
except ValueError:
    print("Invalid Value")