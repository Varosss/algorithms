# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            minNum = nums1
            maxNum = nums2
        else:
            minNum = nums2
            maxNum = nums1

        maxNum.sort()

        answer = []

        def numberIn(nums, number):
            l = 0
            r = len(nums) - 1

            while l < r:
                m = (l + r) // 2

                if nums[m] >= number:
                    r = m
                else:
                    l = m + 1

            if nums[l] == number:
                return True
            
            return False


        for i in range(len(minNum)):
            if numberIn(maxNum, minNum[i]):
                maxNum.remove(minNum[i])
                answer.append(minNum[i])
        
        return answer


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersect(nums1, nums2))