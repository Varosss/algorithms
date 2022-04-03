# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        N = len(s)
        r = 0
        letters = []
        maxLen = 0
        for l in range(N):
            while r < N and s[r] not in letters:
                letters.append(s[r])
                r += 1

            maxLen = max(maxLen, len(letters))
            letters.remove(s[l])

        return maxLen

string = 'abbcdaed'

print(Solution().lengthOfLongestSubstring(string))