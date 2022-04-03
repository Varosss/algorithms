# 4. Median of Two Sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
    
        def addInEvent(event, nums, index):
            event[0] += 1
            event[1] = event[2]
            event[2] = nums[index]


        def answer(event, param):
            if event[0] == param:
                if (m + n) % 2 == 0:
                    return (event[1] + event[2]) / 2

                else:
                    return event[2]


        if (m + n) % 2 == 0:
            param = (m + n + 2) // 2
        else:
            param = (m + n + 1) // 2

        l = 0
        r = 0
        event = [0, 0, 0]

        while l < m and r < n:
            if nums1[l] < nums2[r]:
                l += 1
                addInEvent(event, nums1, l - 1)
            else:
                r += 1
                addInEvent(event, nums2, r - 1)

            return answer(event, param)


        while l < m:
            l += 1
            addInEvent(event, nums1, l - 1)
            return answer(event, param)


        while r < n:
            r += 1
            addInEvent(event, nums2, r - 1)
            return answer(event, param)


nums1 = []
nums2 = [3]

print(Solution().findMedianSortedArrays(nums1, nums2))

#Такое себе решение, но переписывать лень. Зато работает за O(n + m).