import ast
import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(sorted(nums1+nums2))
nums1 = ast.literal_eval(input())
nums2 = ast.literal_eval(input())

sol = Solution()
print(sol.findMedianSortedArrays(nums1,nums2))    