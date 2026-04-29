class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()

        m,n =len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans = max(ans, self.bfs(i,j,grid,seen))
        return ans
    
    def bfs(self,a,b, grid,seen):
        area = 1
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        q = [(a,b)]
        seen.add((a, b))  #
        m,n =len(grid), len(grid[0])
        while q:
            x,y = q.pop()
            for dx,dy in dir:
                new_x = x+dx
                new_y = y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in seen and grid[new_x][new_y]==1:
                    area+=1
                    seen.add((new_x,new_y))
                    q.append((new_x,new_y))
        return area
