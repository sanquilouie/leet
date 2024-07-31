class Solution:
    def isPalindrome(self, x: int) -> bool:
        to_string = str(x)
        if to_string == to_string[::-1]:
            return True
        return False

sol = Solution()
print(sol.isPalindrome(1211))
