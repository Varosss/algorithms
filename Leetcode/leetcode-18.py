# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n):
        combinations = [1, 1]

        for i in range(2, n + 1):
            combinations.append(combinations[i - 2] + combinations[i - 1])

        return combinations[n]

print(Solution().climbStairs(6))