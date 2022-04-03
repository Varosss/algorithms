# 41. First Missing Positive

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        hash = set()

        for i in range(n):
            if nums[i] > 0:
                hash.add(nums[i])

        num = 1

        while True:
            if num not in hash:
                return num
            
            num += 1


nums = [0]

print(Solution().firstMissingPositive(nums))

# Плохое решение