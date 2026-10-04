class Solution(object):

    def generateParenthesis(self, n):

        result = []
        brackets = [""] * (2 * n)

        def solve(index, total):

            # Base case
            if index == len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            # Put (
            brackets[index] = "("
            solve(index + 1, total + 1)

            # Put )
            if total > 0:
                brackets[index] = ")"
                solve(index + 1, total - 1)

        solve(0, 0)

        return result
