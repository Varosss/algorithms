# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n):
        def getPairs(n):
            pairs = []
            for i in range(n):
                pair = ['(', '', ')']
                pairs.append(pair)

            return pairs

        pairs = getPairs(n)

        return pairs

print(Solution().generateParenthesis(3))