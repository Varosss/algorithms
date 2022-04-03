# 389. Find the Difference

class Solution:
    def findTheDifference(self, s, t):
        N = len(t)
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()

        for i in range(N):
            if i < N - 1 and s[i] != t[i]:
                return t[i]

        return t[i]

s = 'abcd'
t = 'abbcd'

print(Solution().findTheDifference(s, t))