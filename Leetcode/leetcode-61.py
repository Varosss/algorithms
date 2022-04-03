# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        def rec(count, obstacleGrid, x, y):
            if obstacleGrid[y][x] == 1:
                return count

            if x == len(obstacleGrid[0]) - 1 and y == len(obstacleGrid) - 1:
                return count + 1

            if x < len(obstacleGrid[y]) - 1:
                count = rec(count, obstacleGrid, x + 1, y)

            if y < len(obstacleGrid) - 1:
                count = rec(count, obstacleGrid, x, y + 1)

            return count

        return rec(0, obstacleGrid, 0, 0)

obstacleGrid = [[1, 0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))