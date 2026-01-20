from typing import List
class Solution:
    def threesum(self, nums: List[int]) -> List[list[int]]:
        output = []
        for i in nums:
            for j in nums:
                for k in nums:
                        a = nums.index(i)
                        b = nums.index(j)
                        c = nums.index(k)
                        if i + j + k == 0 and a != b != c:
                            output.append([i,j,k])
        seen = set()
        unique = []

        for t in output:
            key = tuple(sorted(t))   # canonical representation
            if key not in seen:
                seen.add(key)
                unique.append(list(key))
        return unique

nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
sol = Solution()
print(sol.threesum(nums))