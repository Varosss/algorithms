# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                return [l + 1, r + 1]

            if summ < target:
                l += 1

            if summ > target:
                r -= 1


nums = [2, 7, 11, 15]
target = 13

print(Solution().twoSum(nums, target))