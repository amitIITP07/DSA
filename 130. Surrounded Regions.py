class Solution:

    def dfs(self, r, c, visited, rows, cols, board):

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        if board[r][c] == "X":
            return

        if visited[r][c] == 1:
            return

        visited[r][c] = 1

        # Four directions
        self.dfs(r-1, c, visited, rows, cols, board)
        self.dfs(r, c-1, visited, rows, cols, board)
        self.dfs(r, c+1, visited, rows, cols, board)
        self.dfs(r+1, c, visited, rows, cols, board)

    def solve(self, board):

        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Upper row
        for c in range(cols):
            if board[0][c] == "O" and visited[0][c] == 0:
                self.dfs(0, c, visited, rows, cols, board)

        # Lower row
        for c in range(cols):
            if board[rows-1][c] == "O" and visited[rows-1][c] == 0:
                self.dfs(rows-1, c, visited, rows, cols, board)

        # Left column
        for r in range(rows):
            if board[r][0] == "O" and visited[r][0] == 0:
                self.dfs(r, 0, visited, rows, cols, board)

        # Right column
        for r in range(rows):
            if board[r][cols-1] == "O" and visited[r][cols-1] == 0:
                self.dfs(r, cols-1, visited, rows, cols, board)

        # Convert surrounded O into X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"
