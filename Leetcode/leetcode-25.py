# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, string):
        newString = ''
        for i in range(len(string)):
            if string[i].isalpha():
                newString += string[i].lower()

            if string[i].isdigit():
                newString += string[i]

        for i in range(len(newString) // 2):
            if newString[i] != newString[-i - 1]:
                return False

        return True


print(Solution().isPalindrome('BA'))