# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows):
        pascalsTriangle = []
        for i in range(numRows):
            row = [1]
                
            if i == 1:
                row.append(1)

            if i > 1:
                for j in range(len(pascalsTriangle[i - 1]) - 1):
                    x = pascalsTriangle[i - 1][j] + pascalsTriangle[i - 1][j + 1]
                    row.append(x)

                row.append(1)

            pascalsTriangle.append(row)

        return pascalsTriangle

print(Solution().generate(30))