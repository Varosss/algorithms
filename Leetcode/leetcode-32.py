# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex):
        pascalsTriangle = []
        rowIndex += 1
        for i in range(rowIndex):
            row = [1]
                
            if i == 1:
                row.append(1)

            if i > 1:
                for j in range(len(pascalsTriangle[i - 1]) - 1):
                    x = pascalsTriangle[i - 1][j] + pascalsTriangle[i - 1][j + 1]
                    row.append(x)

                row.append(1)

            pascalsTriangle.append(row)

        return pascalsTriangle[i]

print(Solution().generate(3))