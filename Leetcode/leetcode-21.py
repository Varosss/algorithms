# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1, m, nums2, n):
        if not n:
            return nums1

        for i in range(m + n):
            if nums1[i] == 0 and i >= m:
                nums1[i] = nums2[i - m]

        nums1.sort()

        return nums1

nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
m = 6
nums2 = [1, 2, 5]
n = 3

print(Solution().merge(nums1, m, nums2, n))