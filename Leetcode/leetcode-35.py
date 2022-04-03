# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        numsSet = set()
        for i in range(len(nums)):
            if nums[i] not in numsSet:
                numsSet.add(nums[i])

            else:
                return True

        return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums))