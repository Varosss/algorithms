# 27. Remove Element

class Solution:
    def removeElement(self, nums, val):
        N = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                N -= 1
        
        nums.sort()

        return N, nums

# class Solution:
#     def removeElement(self, nums, val):
#         nums.sort()

#         def binarySearch(nums, val):
#             l = 0
#             r = len(nums) - 1

#             while l < r:
#                 m = (l + r) // 2

#                 if nums[m] >= val:
#                     r = m
                
#                 else:
#                     l = m + 1

#             return l, nums[l]

#         N = len(nums)

#         while val in nums:
#             index, value = binarySearch(nums, val)
#             nums.pop(index)
#             N -= 1

#         return N

nums = [3, 2, 2, 3]
val = 2

print(Solution().removeElement(nums, val))