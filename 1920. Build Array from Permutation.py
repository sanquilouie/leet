from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            ans.append(nums[nums[i]])
            i += 1
        return ans


sol = Solution()
print(sol.buildArray([5,0,1,2,3,4]))