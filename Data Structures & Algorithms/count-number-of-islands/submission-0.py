class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        seen = []
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    ans+=1
                    self.bfs(i,j,seen,grid)
        return ans

    def bfs(self,x,y,seen,grid):
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        q = [(x,y)]
        m,n = len(grid), len(grid[0])
        while q:
            a,b = q.pop()
            grid[a][b]='0'
            for da,db in dir:
                new_a,new_b = a+da, b+db
                if 0<=new_a<m and 0<=new_b<n and (new_a,new_b) not in seen and grid[new_a][new_b]=='1':
                    q.append((new_a,new_b))
        return