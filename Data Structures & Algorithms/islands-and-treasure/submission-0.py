class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        while q:
            r, c = q.popleft()
            for dr, dc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if dr < 0 or dr >= rows or dc < 0 or dc >= cols:
                    continue
                
                if grid[dr][dc] == 2147483647:
                    grid[dr][dc] = grid[r][c] + 1

                    q.append([dr,dc])
                    
        