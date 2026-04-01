nums = [int(x) for x in input("Enter your numbers for array: ").split()]

target = int(input("Enter the target value: "))

output = []

for i in range(len(nums)):
    for j in range(i+ 1, len(nums)):
        if nums[i] + nums[j] == target:
            output.append(i); output.append(j)
            break
    if len(output) > 0:
        break

print(output)