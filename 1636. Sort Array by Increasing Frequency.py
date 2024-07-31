from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        to_dict = Counter(nums)
        sorted_nums = sorted(to_dict.items(), key=lambda item: (item[1], -item[0]))
        for key, count in sorted_nums:
            res.extend([key] * count)
        return res


sol = Solution()
print(sol.frequencySort([-1,1,-6,4,5,-6,1,4,1]))
