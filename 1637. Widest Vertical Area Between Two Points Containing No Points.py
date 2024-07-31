from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = sorted([i[0] for i in points])
        vertical_area = [abs(x_axis[i] - x_axis[i+1]) for i in range(len(x_axis)-1)]
        return max(vertical_area)

sol = Solution()
print(sol.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))