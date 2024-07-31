from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = 0
        min_moves = 0
        while count != len(seats):
            min_moves += abs(seats[count] - students[count])
            count += 1
        return min_moves


sol = Solution()
print(sol.minMovesToSeat([3,1,5], [2,7,4]))