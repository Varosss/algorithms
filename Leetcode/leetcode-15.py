# 66. Plus One

class Solution:
    def plusOne(self, digits):
        N = len(digits)
        answer = []
        num = 0
        for i in range(N):
            num += digits[i]*10**(N - 1 - i)
        
        num += 1

        num = str(num)
        answer = list(num)

        for i in range(len(answer)):
            answer[i] = int(answer[i])

        return answer

digits = [9]
print(Solution().plusOne(digits))