#my approach
# def longest_k_unique(s: str, k: int) -> int:
#     max = 0
#     for i in range(len(s)):
#         output = s[i:]
#         if len(output) > max and len(set(output)) == k:
#             max = len(output)
    
#     return max




# optimized approach
def longest_k_unique(s: str, k: int) -> int:
    left = 0
    freq = {}
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


s = input("Enter your String: ")
k = int(input("Target Value: "))

print(longest_k_unique(s=s,k=k))