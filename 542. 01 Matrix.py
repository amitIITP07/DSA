class Solution(object):
    def updateMatrix(self, mat):

        rows = len(mat)
        cols = len(mat[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        distance = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = deque()

        # Step 1: Add all zeroes into queue
        for r in range(rows):
            for c in range(cols):

                if mat[r][c] == 0:
                    queue.append([r, c, 0])
                    visited[r][c] = 1

        # Four directions
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # Step 2: BFS
        while queue:

            i, j, d = queue.popleft()

            distance[i][j] = d

            for dr, dc in directions:

                new_i = i + dr
                new_j = j + dc

                # Boundary check
                if (new_i < 0 or new_i >= rows or
                    new_j < 0 or new_j >= cols):
                    continue

                # Already visited
                if visited[new_i][new_j] == 1:
                    continue

                queue.append([new_i, new_j, d + 1])

                visited[new_i][new_j] = 1

        return distance
