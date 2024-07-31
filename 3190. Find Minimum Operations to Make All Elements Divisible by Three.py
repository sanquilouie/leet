from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_count = 0
        for i in nums:
            if i % 3 != 0:
                min_count += 1
        return min_count



sol = Solution()
print(sol.minimumOperations([1,2,3,4]))