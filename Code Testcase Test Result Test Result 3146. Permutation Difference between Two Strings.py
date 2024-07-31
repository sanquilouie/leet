class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        list_t = [i for i in t]
        sum_perm = 0

        for index, value in enumerate(s):
            sum_perm += abs(index - list_t.index(value))
        return sum_perm




sol = Solution()
print(sol.findPermutationDifference("abcde", "edbac"))