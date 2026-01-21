import ast
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        return statistics.median(nums1+nums2)

nums1 = ast.literal_eval(input())
nums2 = ast.literal_eval(input())

sol = Solution()
print(sol.findMedianSortedArrays(nums1,nums2))

sol1 = Solution()
    