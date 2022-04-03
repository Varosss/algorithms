# 136. Single Number

class Solution:
    def singleNumber(self, nums):
        N = len(nums)
        dict = {}

        for i in range(N):
            if nums[i] not in dict:
                dict[nums[i]] = 0
            dict[nums[i]] += 1

        for key in dict:
            if dict[key] == 1:
                return key


nums = [1, 1, 2, 2, 6, 6, 3, 9, 8, 9, 8]
print(Solution().singleNumber(nums))