# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n):
        l = 0
        r = 30

        while l < r:
            m = (l + r) // 2

            if 3**m >= n:
                r = m
            else:
                l = m + 1

        if 3**l == n:
            return True

        return False


print(Solution().isPowerOfThree(1291401635435))