# 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word):
        count = 0
        for i in range(len(word)):
            if word[i].isupper():
                count += 1

        if count == len(word):
            return True

        if count == 0:
            return True

        if count == 1 and word[0].isupper():
            return True

        return False


string = 'Google'
print(Solution().detectCapitalUse(string))