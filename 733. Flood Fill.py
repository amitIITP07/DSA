class Solution(object):
    def floodFill(self, image, sr, sc, color):

        rows = len(image)
        cols = len(image[0])

        original_color = image[sr][sc]

        # Already same color
        if original_color == color:
            return image

        def dfs(r, c):

            # Boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Different color
            if image[r][c] != original_color:
                return

            # Change color
            image[r][c] = color

            # Visit four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        dfs(sr, sc)

        return image
