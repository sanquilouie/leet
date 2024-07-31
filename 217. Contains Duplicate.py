from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


sol = Solution()
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))