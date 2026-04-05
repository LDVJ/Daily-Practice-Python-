value = list(input("Enter your word: ").strip())

n = len(value)

output_lst = []

for i in range(n-1, -1, -1):
    output_lst.append(value[i])

print("".join(output_lst))
    
