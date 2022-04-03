# 242. Valid Anagram

class Solution:
    def isAnagram(self, s, t):
        def makeDictOfStr(string):
            dict = {}
            for i in range(len(string)):
                if string[i] not in dict:
                    dict[string[i]] = 0
                dict[string[i]] += 1

            return dict

        dictS = makeDictOfStr(s)
        dictT = makeDictOfStr(t)

        if dictS == dictT:
            return True
        
        return False

s = 'rat'
t = 'rat'

print(Solution().isAnagram(s, t))