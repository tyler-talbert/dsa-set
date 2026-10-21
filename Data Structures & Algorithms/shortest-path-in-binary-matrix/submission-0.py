class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        if grid[ROWS - 1][COLS - 1] != 0 or grid[0][0] != 0:
            return -1
        # Only visit 0
        # Vertical, horizontal, diagonal
        # return num visited in the path

        q = collections.deque([(0, 0, 1)])
        grid[0][0] = 1
        while q:
            r, c, path_length = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return path_length
            
            for x, y in DIRECTIONS:
                nr, nc = x + r, y + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, path_length + 1))
        
        return -1


        