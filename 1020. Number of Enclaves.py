from collections import deque

class Solution:
    def numEnclaves(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        queue = deque()

        # Step 1: Add boundary land cells
        for r in range(rows):
            for c in range(cols):

                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:

                    if grid[r][c] == 1:
                        queue.append((r, c))
                        visited[r][c] = 1

        # Step 2: BFS traversal
        while queue:

            i, j = queue.popleft()

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:

                new_i = i + dx
                new_j = j + dy

                # Check boundaries
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue

                # Check water
                if grid[new_i][new_j] == 0:
                    continue

                # Check visited
                if visited[new_i][new_j] == 1:
                    continue

                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))

        # Step 3: Count enclaves
        count = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1

        return count
