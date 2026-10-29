class Solution:
    def spiralOrder(self, grid: List[List[int]]) -> List[int]:
        if len(grid) == 1:
            return grid[0]

        DIRECTIONS = ["RIGHT", "DOWN", "LEFT", "UP"]

        ROWS, COLS = len(grid), len(grid[0])
        res = []
        r, c = 0, -1

        while ROWS > 0 and COLS > 0:
            for i in range(len(DIRECTIONS)):
                direction = DIRECTIONS[i]
                
                if ROWS > 0 and COLS > 0:
                    if direction == "RIGHT":
                        for _ in range(COLS):
                            c += 1
                            res.append(grid[r][c])
                        ROWS -= 1
                    elif direction == "DOWN":
                        for _ in range(ROWS):
                            r += 1
                            res.append(grid[r][c])
                        COLS -= 1
                    elif direction == "LEFT":
                        for _ in range(COLS):
                            c -= 1
                            res.append(grid[r][c])
                        ROWS -= 1
                    else:
                        for _ in range(ROWS):
                            r -= 1
                            res.append(grid[r][c])
                        COLS -= 1
                else:
                    return res
        
        return res
        
        #  COLS
        # [1,2,3]
        # [4,5,6] ROWS
        # [7,8,9]

        # Stage 1 
        # 3 ROWS, 3 COLS
        # Stage 2
        # 2 ROWS, 3 COLS
        # Stage 3
        # 2 ROWS, 2 COLS
        # STAGE 4
        # 1 ROW, 2 COLS
        # STAGE 5
        # 1 ROW, 1 COL




        