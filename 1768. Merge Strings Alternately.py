class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word2 = [x for x in word2]
        res = ""
        for i in range(len(word1)):
            res += word1[i] + word2[i]
        return res


sol = Solution()
print(sol.mergeAlternately("ab", "pqrs"))