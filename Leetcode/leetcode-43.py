# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s):
        chars = {}
        length = 0
        for char in s:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1

        values = sorted(chars.values(), reverse=True)
        stock = 0

        for i in range(len(values)):
            if values[i] % 2 == 0:
                length += values[i]

            if values[i] > 1 and values[i] % 2 != 0:
                length += values[i] - 1
                stock += 1

            if values[i] == 1:
                length += 1
                return length

        if length % 2 == 0 and stock > 0:
            length += 1
        
        return length

string = 'сс'
print(Solution().longestPalindrome(string))