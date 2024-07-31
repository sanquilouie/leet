from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        add_rungs = 0
        prev_height = 0
        for rung in rungs:
            gap = rung-prev_height
            if gap > dist:
                add_rungs += (gap-1) // dist
            prev_height = rung
        return add_rungs


sol = Solution()
print(sol.addRungs([1,3,5,12], 2))
