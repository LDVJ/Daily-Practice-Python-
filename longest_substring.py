def longest_k_unique(s: str, k: int) -> int:
    max = 0
    for i in range(len(s)):
        output = s[i:]
        if len(output) > max and len(set(output)) == k:
            max = len(output)
    
    return max

s = input("Enter your String: ")
k = int(input("Target Value: "))

print(longest_k_unique(s=s,k=k))