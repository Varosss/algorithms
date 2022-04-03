# 202. Happy Number

class Solution:
    def isHappy(self, n):
        nums = set()

        while True:
            if n == 1:
                return True
            
            if n in nums:
                return False

            nums.add(n)

            sum = 0
            while n > 0:
                sum += (n % 10)**2
                n //= 10
            
            n = sum
        
num = 10
print(Solution().isHappy(num))