# 509. Fibonacci Number

class Solution:
    def fib(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n > 1:
            return Solution().fib(n - 2) + Solution().fib(n - 1)

print(Solution().fib(30))