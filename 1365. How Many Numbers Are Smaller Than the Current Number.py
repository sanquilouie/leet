from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        return sorted_nums, nums



sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))