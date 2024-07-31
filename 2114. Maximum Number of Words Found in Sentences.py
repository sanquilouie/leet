from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        highest_value = 0
        for i in sentences:
            value = i.count(" ")
            if value > highest_value:
                highest_value = value
        return highest_value + 1


sol = Solution()
print(sol.mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))
