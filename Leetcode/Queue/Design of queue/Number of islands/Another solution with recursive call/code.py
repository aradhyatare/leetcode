class Solution:
    def numIslands(self, grid) -> int:
        m,n=len(grid),len(grid[0])
        islands=0
        def visit(r,c):
            grid[r][c]="2"
            if r<m-1:
                if grid[r+1][c]=="1":
                    visit(r+1,c)
            if r>0: 
                if grid[r-1][c]=="1": 
                    visit(r-1,c)
            if c<n-1:
                if grid[r][c+1]=="1": 
                    visit(r,c+1)
            if c>0: 
                if grid[r][c-1]=="1": 
                    visit(r,c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1": 
                    islands+=1
                    visit(i,j)
        return islands