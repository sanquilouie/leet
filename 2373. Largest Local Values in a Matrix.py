from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local = []
        temp_local = []
        for i in range(len(grid)-2):
            for j in range(len(grid[i])-2):
                temp_local.append(max([grid[i][j], grid[i][j+1], grid[i][j+2],
                                       grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                                       grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]]))
            max_local.append(temp_local)
            temp_local = []
        return max_local


sol = Solution()
print(sol.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))