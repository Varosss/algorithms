# 258. Add Digits

class Solution:
    def addDigits(self, num):
        if num < 10:
            return num

        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10

        return Solution().addDigits(sum)

print(Solution().addDigits(123))