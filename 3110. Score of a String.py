class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for j in range(len(s)-1):
            res += abs(ord(s[j]) - ord(s[j+1]))
        return res


sol = Solution()
print(sol.scoreOfString("hello"))
