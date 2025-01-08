class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()

        rows, cols = len(heights), len(heights[0])

        def spread(r, c, land):
            land.add((r,c))
            dirs = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))

            for dr, dc in dirs:
                if (
                    0 <= dr < rows and
                    0 <= dc < cols and
                    heights[dr][dc] >= heights[r][c]
                    and (dr, dc) not in land
                ):
                    spread(dr, dc, land)
            
        for row in range(rows):
            spread(row, 0, pac)
            spread(row, cols - 1, atl)
        for col in range (cols):
            spread(0, col, pac)
            spread(rows - 1, col, atl)
        
        return list(atl & pac)