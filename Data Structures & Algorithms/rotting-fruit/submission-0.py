class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for nr, nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if nr >= rows or nr < 0 or nc >= cols or nc < 0:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr,nc])
                
            minutes += 1

        if fresh == 0:
            return minutes
        return -1
        