from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            if not any(r[0] <= i <= r[1] for r in ranges):
                return False
        return True


sol = Solution()
print(sol.isCovered([[1,1]], 1, 50))

