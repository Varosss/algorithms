# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1, nums2):
        answer = []

        nums1.sort()

        def elementInList(list, num):
            l = 0
            r = len(list) - 1

            while l < r:
                m = (l + r) // 2

                if list[m] >= num:
                    r = m
                
                else:
                    l = m + 1

            if list[l] == num:
                return True

            return False


        for i in range(len(nums2)):
            if elementInList(nums1, nums2[i]) and nums2[i] not in answer:
                answer.append(nums2[i])

        return answer


nums1 = [1, 5, 8, 9, 12]
nums2 = [2, 1, 4, 2, 5]

print(Solution().intersection(nums1, nums2))