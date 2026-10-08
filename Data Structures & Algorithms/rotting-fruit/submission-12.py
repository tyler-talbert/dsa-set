class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        mins = 0
        fresh_fruits = 0
        q = collections.deque()
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        
        while q:
            r, c, time = q.popleft()
            mins = time
            grid[r][c] = 2
            for x, y in DIRECTIONS:
                nr, nc = x + r, y + c
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if (nr, nc) not in seen and grid[nr][nc] == 1:
                    seen.add((nr, nc))
                    fresh_fruits -= 1
                    q.append((nr, nc, time + 1))

        return mins if fresh_fruits == 0 else -1





        