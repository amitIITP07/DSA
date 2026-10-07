class Solution(object):
    def solveNQueens(self, n):

        result = []

        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):

            # Check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check upper-left diagonal
            i = row - 1
            j = col - 1

            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i = row - 1
            j = col + 1

            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(row):

            # All queens placed
            if row == n:
                solution = []

                for r in board:
                    solution.append("".join(r))

                result.append(solution)
                return

            # Try every column
            for col in range(n):

                if is_safe(row, col):

                    # Choose
                    board[row][col] = "Q"

                    # Explore
                    solve(row + 1)

                    # Undo
                    board[row][col] = "."

        solve(0)

        return result
