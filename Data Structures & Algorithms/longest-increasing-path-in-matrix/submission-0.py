class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or  not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            max_length = 1

            for dr, dc in directions:
                nr, nc = r+ dr, c+dc
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
                    max_length = max(max_length, 1+ dfs(nr,nc))
            
            memo[(r,c)] = max_length
            return max_length
        
        max_path = 0
        for r in range(rows):
            for c in range(cols):
                max_path = max(max_path, dfs(r,c))
        return max_path