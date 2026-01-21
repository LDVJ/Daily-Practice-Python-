# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
import ast

# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         CurrArea = 1
#         n = len(height)-1
#         i = 0
#         MaxArea = 0
#         while i< n:
#             h = min(height[i],height[n])
#             w = n-i
#             CurrArea = h * w
#             MaxArea = max(CurrArea, MaxArea)
        
#         if height[i] < height[n]:
#             i +=1 
#         else:
#             n -= 1

        
#         return MaxArea

# print(len(height))



from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best = 0

        while l < r:
            hl = height[l]
            hr = height[r]
            width = r - l

            if hl < hr:
                area = hl * width
                if area > best:
                    best = area
                l += 1
            else:
                area = hr * width
                if area > best:
                    best = area
                r -= 1

        return best

height = ast.literal_eval(input())
sol = Solution()
print(sol.maxArea(height))