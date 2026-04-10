def first_unique_char(s: str) -> int:
    index = -1
    lst  = s[:]
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j] and i != j:
                break
        else:
            return i
    
    return index
                
s = input("Enter your string: ")
print(first_unique_char(s=s))