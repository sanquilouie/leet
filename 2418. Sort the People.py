from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        to_tuple = list(zip(names, heights))
        sorted_tuple = sorted(to_tuple, key=lambda item: item[1], reverse=True)
        return [key for key, _ in sorted_tuple]


sol = Solution()
print(sol.sortPeople(["Alice","Bob","Bob"], [155,185,150]))