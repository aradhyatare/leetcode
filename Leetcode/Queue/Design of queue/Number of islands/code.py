import collections


class Solution:
    def numIslands(self, grid) -> int:

        rows, cols = len(grid), len(grid[0])
        visit = set()
        isisland = 0
        directions = [[1,0], [0,1],[-1,0],[0,-1]]

        def BFS(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r,c =row +dr, col + dc
                    if (r in range(rows) and c  in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    BFS(row,col)
                    isisland += 1
        
        return isisland


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Myobj = Solution()
var = Myobj.numIslands(grid)
print(var)