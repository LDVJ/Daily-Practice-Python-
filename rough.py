# from typing import List
# import ast

# def threesum(nums: List[int])-> List[List[int]]:
#     nums.sort()
#     output = []
#     n = len(nums)

#     for i in range(n):
#         if nums[i]> 0:
#             break
#         if i > 0 and nums[i] == nums[i-1]:
#             continue

#         l,r = i+1,n-1
#         while l < r:
#             sum = nums[i]+nums[l]+nums[r]

#             if sum <0:
#                 l += 1
#             elif sum > 0:
#                 r -= 1
#             else:
#                 output.append([nums[i],nums[l],nums[r]])
#                 l += 1
#                 r -= 1
#                 while l < r and nums[l] == nums[l-1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r+1]:
#                     r -= 1

#     print(output)

# nums = ast.literal_eval(input("Enter the List: "))
# threesum(nums)

# a = ""
# b = " "
# print(a == b)

# import os

# path = os.getenv("LOCAL_DB_URL")

# print(path)


