# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         output = ''
        # for i in True:
            

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         strs.sort()
#         a, b = strs[0], strs[-1]
#         i = 0
#         while i < len(a) and i < len(b) and a[i] == b[i]:
#             i += 1
#         return a[:i]
        
arr = ["abcdrha","bababara","abchra",'bababar','bababa']
print(arr.sort())
print(arr)


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
