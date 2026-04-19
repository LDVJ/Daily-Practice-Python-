# value = list(input("Enter your value to check: ").replace(" ","").lower().strip())

# check = []

# for i in range(len(value)-1, -1, -1):
#     check.append(value[i])

# print(value == check)
# print("".join(value) == "".join(check))


# optimization
value = input("Ente your word: ").strip()

def check_palindrome(value : str) -> bool:
    i = 0
    j = len(value) - 1

    while i < j:
        if value[i] != value[j] and i != j:
            return False
        else:
            i += 1
            j -= 1

    return True