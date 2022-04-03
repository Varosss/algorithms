# 47. Permutations II

class Solution:
    def permuteUnique(self, nums):
        output = []
        dict = {}

        for el in nums:
            if el not in dict:
                dict[el] = 0
            dict[el] += 1

        def rec(dict, N, List):
            if len(List) == N:
                output.append(List)
                return

            for key in dict:
                if dict[key] > 0:
                    newList = List.copy()
                    newList.append(key)
                    dict[key] -= 1
                    rec(dict, N, newList)
                    dict[key] += 1

        rec(dict, len(nums), [])

        return output

nums = [1, 2, 3, 4]
print(Solution().permuteUnique(nums))