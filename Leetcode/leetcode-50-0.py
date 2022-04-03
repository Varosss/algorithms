# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, nums, target):
        def binarySearch(l, r, nums, sum, target):
            while l < r:
                m = (l + r) // 2

                if sum + nums[m] >= target:
                    r = m
                
                else:
                    l = m + 1

            return l
        

        for i in range(len(nums) - 1):
            j = binarySearch(i + 1, len(nums) - 1, nums, nums[i], target)

            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]

nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))