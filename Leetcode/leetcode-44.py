# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern, string):
        patternList = list(pattern)
        stringList = list(string.split())

        if len(patternList) != len(stringList):
            return False

        patternSet = set(patternList)
        stringSet = set(stringList)

        if len(patternSet) != len(stringSet):
            return False

        
        for i in range(len(patternList) - 1):
            if patternList[i] == patternList[i + 1] and stringList[i] != stringList[i + 1]:
                return False
            
            elif patternList[i] != patternList[i + 1] and stringList[i] == stringList[i + 1]:
                return False

        return True

string = 'dog cat cat dog'
pattern = 'aaaa'

print(Solution().wordPattern(pattern, string))