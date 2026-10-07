class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c,ocean):
            ocean.add((r,c))
        
            for dr, dc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if dr < 0 or dr >= rows or dc < 0 or dc >= cols:
                    continue
                if (dr,dc) in ocean:
                    continue

                if heights[dr][dc] < heights[r][c]:
                    continue
                dfs(dr,dc,ocean)

        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)

        for r in range(rows):
            dfs(r,cols-1,atlantic)
        for c in range(cols):
            dfs(rows-1,c,atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append([r,c])

        return result

            


        