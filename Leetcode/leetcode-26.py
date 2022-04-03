# 268. Missing Number

class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] != i:
                return i

        return n

nums = [9,6,4,2,3,5,7,0,1]
print(Solution().missingNumber(nums))