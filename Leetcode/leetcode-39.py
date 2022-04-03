# 704. Binary Search

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] >= target:
                r = m
            else:
                l = m + 1

        if nums[l] == target:
            return l

        return -1

nums = [-1,0,3,5,9,12]
target = 2

print(Solution().search(nums, target))