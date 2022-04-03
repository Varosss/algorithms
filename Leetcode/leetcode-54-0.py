# 62. Unique Paths

class Solution:
    def uniquePaths(self, m, n):
        def rec(left, down, count=0):
            if left == down == 0:
                return count + 1

            if left > 0:
                count += rec(left - 1, down)

            if down > 0:
                count += rec(left, down - 1)
            
            return count
        
        return rec(m - 1, n - 1)

print(Solution().uniquePaths(10, 10))