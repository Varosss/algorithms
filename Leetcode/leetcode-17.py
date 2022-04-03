# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x):
        l = 0
        r = 2**31 - 1

        while l < r:
            m = (l + r) // 2

            if m*m >= x:
                r = m
            
            else:
                l = m + 1

        if l*l > x:
            l -= 1
            
        return l

print(Solution().mySqrt(8))