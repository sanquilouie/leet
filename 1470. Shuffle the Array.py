from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        first = nums[:n]
        second = nums[n:]
        for i in range(len(nums) // 2):
            output.append(first[i])
            output.append(second[i])
        return output



sol = Solution()
print(sol.shuffle([1,2,3,4,4,3,2,1], 4))
