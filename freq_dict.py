text = input("Enter your value: ").strip().lower()

char_freq = {}

for item in text:
    char_freq[item] = char_freq.get(item, 0) + 1
 
# for item in list(char_freq):
#     if char_freq[item] == 1:
#         char_freq.pop(item)

# creating new dict instead of removing one

result = {item : value for item, value in char_freq.items() if value > 1}

print(result)