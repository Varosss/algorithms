# 58. Length of Last Word

class Solution:
    def lengthOfLastWord(self, s):
        word = ''
        lastWord = ''
        N = len(s)
        for i in range(N):
            if s[i] != ' ':
                word += s[i]
            
            if (s[i] == ' ' or i == N - 1) and word:
                lastWord = word
                word = ''

        answer = len(lastWord)

        return answer

string = 'luffy is still joyboy'

print(Solution().lengthOfLastWord(string))