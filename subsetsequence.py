s = "abcde"
words = ["a","bb","acd","ace"]

count = 0

for word in words:
    i = j = 0
    while i < len(word) and j < len(s):
        if word[i] == s[j]:
            i += 1
        j += 1

    if i == len(word):
        count += 1
     

print("Count : ", count)