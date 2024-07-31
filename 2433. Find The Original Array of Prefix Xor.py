from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        temp_pref = [pref[0]]
        for i in range(1, len(pref)):
            temp_pref.append(pref[i - 1] ^ pref[i])
        return temp_pref

sol = Solution()
print(sol.findArray([5]))
