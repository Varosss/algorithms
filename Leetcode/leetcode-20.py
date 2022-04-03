# 344. Reverse String

class Solution:
    def reverseString(self, s):
        N = len(s) // 2
        for i in range(N):
            s[i], s[-i - 1] = s[-i - 1], s[i]

        return s

print(Solution().reverseString(["H","a","n","n","a","h"]))