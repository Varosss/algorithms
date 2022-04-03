# 46. Permutations

class Solution:
    def permute(self, nums):
        output = []

        def rec(nums, N, List):
            if len(List) == N:
                output.append(List)
                return

            for i in range(len(nums)):
                newList = List.copy()
                newList.append(nums[i])
                rec(nums[: i] + nums[i + 1:], N, newList)

        rec(nums, len(nums), [])

        return output


nums = [1, 2, 3]
print(Solution().permute(nums))