# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums):
        helper = set()
        for i in range(len(nums)):
            if nums[i] not in helper:
                helper.add(nums[i])
            else:
                nums[i] = 101

        nums.sort()
        k = len(helper)

        return k