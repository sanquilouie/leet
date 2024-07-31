from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = 0
        while nums:
            if nums[counter] not in result[counter]:
                result.append([nums[counter]])
            else:
                result[counter].extend([nums[counter]])
            nums.pop(counter)
            counter += 1


sol = Solution()
print(sol.findMatrix([1,3,4,1,2,3,1]))