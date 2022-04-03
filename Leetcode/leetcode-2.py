# 1. Two Sum

class Solution:
    def twoSum(self, nums, target):
        output = []
        newNums = nums.copy()
        newNums.sort()

        def binarySearch(l, r, nums, sum, target):
            while l < r:
                m = (l + r) // 2

                if sum + nums[m] >= target:
                    r = m
                
                else:
                    l = m + 1

            return l


        def findNums(nums, target):
            for i in range(len(nums) - 1):
                j = binarySearch(i + 1, len(nums) - 1, nums, nums[i], target)

                if nums[i] + nums[j] == target:
                    return nums[i], nums[j]


        num1, num2 = findNums(newNums, target)

        for i in range(len(nums)):
            if (nums[i] == num1 or nums[i] == num2) and i not in output:
                output.append(i)

        return output


nums = [0, 3, 4, 0]
target = 0

print(Solution().twoSum(nums, target))