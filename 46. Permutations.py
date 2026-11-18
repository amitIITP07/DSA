class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, remaining):

            if not remaining:
                result.append(path[:])
                return

            for i in range(len(remaining)):

                num = remaining[i]

                new_remaining = remaining[:i] + remaining[i+1:]

                backtrack(path + [num], new_remaining)

        backtrack([], nums)

        return result
