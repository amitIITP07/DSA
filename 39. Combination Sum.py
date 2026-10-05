class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def solve(index, total, subset):

            if total == target:
                result.append(subset[:])
                return

            if total > target or index >= len(candidates):
                return

            # Take
            subset.append(candidates[index])

            solve(
                index,
                total + candidates[index],
                subset
            )

            # Backtrack
            subset.pop()

            # Skip
            solve(
                index + 1,
                total,
                subset
            )

        solve(0, 0, [])

        return result
