value = list(input("Enter your value to check: ").replace(" ","").lower().strip())

check = []

for i in range(len(value)-1, -1, -1):
    check.append(value[i])

print(value == check)
# print("".join(value) == "".join(check))