# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums, target):
        
        def findPivot(nums):
            m = (len(nums) - 1) // 2

            if nums[0] > nums[-1]:
                while True:
                    if nums[m] > nums[m + 1]:
                        return m

                    if nums[m] < nums[m - 1]:
                        return m - 1

                    if nums[m] < nums[m + 1] and nums[m] > nums[0]:
                        m += 1

                    if nums[m] < nums[m + 1] and nums[m] < nums[0]:
                        m -= 1

            return -1

        
        def binarySearch(l, r, nums, target):
            while l < r:
                m = (l + r) // 2

                if nums[m] >= target:
                    r = m
                
                else:
                    l = m + 1

            return l


        pivot = findPivot(nums)

        if pivot > -1:
            targetId1 = binarySearch(0, pivot, nums, target)
            targetId2 = binarySearch(pivot + 1, len(nums) - 1, nums, target)

            if nums[targetId1] == target:
                return targetId1

            if nums[targetId2] == target:
                return targetId2

            return -1

        if pivot == -1:
            targetId = binarySearch(0, len(nums) - 1, nums, target)

            if nums[targetId] == target:
                return targetId

            return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 1
print(Solution().search(nums, target))