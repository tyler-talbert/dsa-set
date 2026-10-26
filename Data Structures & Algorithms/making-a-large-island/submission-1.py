import collections
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sizes = collections.defaultdict(int)
        res = 0
        id = 1

        def dfs(r, c, island):
            grid[r][c] = island
            size = 0
            stack = [(r, c)]

            while stack:
                r, c = stack.pop()
                size += 1

                for x, y in DIRECTIONS:
                    nr, nc = x + r, c + y
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = island
                        stack.append((nr, nc))

            return size
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    id += 1
                    sizes[id] = dfs(r, c, id)
                    res = max(res, sizes[id])

        # find the largest island possible
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # Check its neighbors
                    neighbor_islands = set()
                    for x, y in DIRECTIONS:
                        nr, nc = x + r, c + y
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] in sizes:
                            neighbor_islands.add(grid[nr][nc])
                    res = max(res, 1 + sum(sizes[island_id] for island_id in neighbor_islands))

        return res
                             

