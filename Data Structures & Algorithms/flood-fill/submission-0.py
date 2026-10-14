class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]
        if starting_color == color:
            return image
            
        ROWS, COLS = len(image), len(image[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def fill(r, c):
            image[r][c] = color

            for x, y in DIRECTIONS:
                nr, nc = x + r, y + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == starting_color:
                    fill(nr, nc)
            

        fill(sr, sc)
        return image
        

        
        