# 1394. Find Lucky Integer in an Array

class Solution:
    def findLucky(self, arr):
        N = len(arr)
        numOfNums = {}
        answer = -1

        for i in range(N):
            if arr[i] not in numOfNums:
                numOfNums[arr[i]] = 0
            numOfNums[arr[i]] += 1

        for num in numOfNums:
            if numOfNums[num] == num:
                answer = max(answer, num)

        return answer

print(Solution().findLucky([2, 2, 2, 3, 3]))