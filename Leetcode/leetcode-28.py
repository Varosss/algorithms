# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        l = 0
        r = 31

        while l < r:
            m = (l + r) // 2

            if 2**m >= n:
                r = m
            
            else:
                l = m + 1

        if 2**l == n:
            return True

        return False


print(Solution().isPowerOfTwo(64))