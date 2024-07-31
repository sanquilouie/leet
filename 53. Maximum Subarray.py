from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_nums = 0
        for i in nums:
            curr_sum += i
            if curr_sum > max_nums:
                max_nums = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_nums


sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))