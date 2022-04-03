# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        prefixes = {}
        for letter in strs:
            for i in range(len(letter)):
                pref = letter[:i + 1]
                if pref not in prefixes:
                    prefixes[pref] = 0
                prefixes[pref] += 1

        mostCommon = 0
        answer = ''
        for key in prefixes:
            if prefixes[key] > mostCommon:
                mostCommon = prefixes[key]
                answer = key

            elif prefixes[key] == mostCommon and len(key) > len(answer):
                answer = key

        if mostCommon < len(strs):
            answer = ''

        return answer

print(Solution().longestCommonPrefix(["reflower","flow","flight"]))

#Плохое решение, условие не так понял, но зато память почти не тратит, круто?