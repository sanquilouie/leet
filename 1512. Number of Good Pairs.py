from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good_pairs += 1
        return good_pairs


sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))