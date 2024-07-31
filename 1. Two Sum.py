from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, value in enumerate(nums):
            comp = target - value
            print(target, '-',  value, ' = ', comp)
            print(hashtable)
            if comp in hashtable:
                return [hashtable[comp], index]
            else:
                hashtable[value] = index


sol = Solution2()
print(sol.twoSum([3,2,4], 6))
