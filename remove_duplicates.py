value = list(input("Enter your list Value: "))
# value = [1, "1", 1]

output = []

for chr in value:
    if chr not in output and chr != " ":
        output.append(chr)

print(output)