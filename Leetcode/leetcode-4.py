# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        chars = list(x)
        y = ''

        for i in range(len(chars) - 1, -1, -1):
            y += chars[i]

        if x == y:
            return True

        return False

print(Solution().isPalindrome(111121111))