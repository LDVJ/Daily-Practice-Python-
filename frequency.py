value =  input("Enter you value: ").strip()

output = {}

for chr in value:
    if chr not in output:
        output[chr] = 1
    # elif chr == " ": # in case we don't need spaces
    #     continue
    else:
        output[chr] += 1

print(output)