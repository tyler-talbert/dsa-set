class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0
        seen = set()

        def dfs(r, c):
            if (r, c) in seen:
                return 0
            
            seen.add((r, c))
            grid[r][c] = 0

            for x, y in DIRECTIONS:
                nr, nc = x + r, y + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    dfs(nr, nc)
                
            return 1



        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == "1":
                    islands += dfs(r, c)
        
        return islands
        