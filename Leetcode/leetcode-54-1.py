# 62. Unique Paths

class Solution:
    def uniquePaths(self, m, n):
        def rec(m, n, paths=[1]*n, count=1):
            if m == count:
                return paths[-1]

            for i in range(1, n):
                paths[i] = paths[i - 1] + paths[i]

            return rec(m, n, paths, count + 1)

        return rec(m, n)

print(Solution().uniquePaths(100, 100))