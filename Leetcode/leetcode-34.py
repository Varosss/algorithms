# 28. Implement strStr()

class Solution:
    def strStr(self, haystack, needle):
        N = len(needle)

        if haystack == needle:
            return 0

        for i in range(len(haystack) - N + 1):
            if haystack[i: i + N] == needle:
                return i

        return -1

haystack = 'abc'
needle = 'c'

print(Solution().strStr(haystack, needle))