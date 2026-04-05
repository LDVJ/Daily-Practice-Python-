value = list(input("Enter your list Value: ").split(" "))
# value = [1, "1", 1]

output = []

for item in value:
    if item.isdigit() or (item.startswith("-") and item.lstrip("-").isdigit()):
        item = int(item)
    if item not in output and item != " ":
        output.append(item)

print(output)