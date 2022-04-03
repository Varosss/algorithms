# 11. Container With Most Water

class Solution:
    def maxArea(self, height):
        N = len(height)
        mostWaterContained = 0
        waterContained = 0
        
        l = 0
        r = N - 1

        while l < N and r > 0 and l < r:
            w = r - l
            h = min(height[l], height[r])

            waterContained = h * w
            mostWaterContained = max(waterContained, mostWaterContained)

            if height[l] > height[r]:
                r -= 1

            else:
                l += 1

        return mostWaterContained


height = [7, 1, 2, 3, 4, 5, 4]
print(Solution().maxArea(height))