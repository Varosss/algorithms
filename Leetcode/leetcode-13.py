# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m
            
            else:
                l = m + 1

        return l

nums = [1, 3, 5, 6]
target = 2

print(Solution().searchInsert(nums, target))