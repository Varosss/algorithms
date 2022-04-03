# 15. 3Sum

class Solution:
    def threeSum(self, nums):
        nums.sort()
        output = set()

        for l in range(len(nums)):
            target = -nums[l]
            m = l + 1
            r = len(nums) - 1
        
            while m < r:
                summ = nums[m] + nums[r]

                if summ == target:
                    output.add((nums[l], nums[m], nums[r]))
                    m += 1
                    r -= 1

                if summ < target:
                    m += 1

                if summ > target:
                    r -= 1

        return output

nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
print(Solution().threeSum(nums))