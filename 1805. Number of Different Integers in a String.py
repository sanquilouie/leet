import re


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(int(sub) for sub in re.sub(r'\D', ' ', word).split() if sub))


sol = Solution()
print(sol.numDifferentIntegers("a1b01c001"))
