# 169. Majority Element

class Solution:
    def majorityElement(self, nums):
        N = len(nums)
        dict = {}

        for i in range(N):
            if nums[i] not in dict:
                dict[nums[i]] = 0
            dict[nums[i]] += 1

            if dict[nums[i]] > N // 2:
                return nums[i]

nums = [6,6,6,7,7]
print(Solution().majorityElement(nums))