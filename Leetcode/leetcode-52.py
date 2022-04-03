# 75. Sort Colors

class Solution:
    def sortColors(self, nums, count=1):
        if count > 0:
            count = 0
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    count += 1

            return Solution().sortColors(nums, count)

        return nums

nums = [2,0,1]

print(Solution().sortColors(nums))