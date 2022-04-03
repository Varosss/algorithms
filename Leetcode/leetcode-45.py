# 342. Power of Four

class Solution:
    def isPowerOfFour(self, n):
        l = 0
        r = 16

        while l < r:
            m = (l + r) // 2

            if 4**m >= n:
                r = m
            else:
                l = m + 1

        if 4**l == n:
            return True

        return False

print(Solution().isPowerOfFour(387420488))