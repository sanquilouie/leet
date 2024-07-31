from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        with_x = []
        for index, value in enumerate(words):
            if x in value:
                with_x.append(index)
        return with_x
                

sol = Solution()
print(sol.findWordsContaining(words=["abc","bcd","aaaa","cbc"], x="z"))
