class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        count = 0
        for i in range (m) :
            for j in range(n) :
                if grid[i][j] == "1" :
                    count +=1
                    self.dfs(i , j , grid , m , n)
        return count
    def dfs(self , i ,j ,grid , m , n) :
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' :
            return
        grid[i][j] = '0'
        self.dfs(i - 1 , j , grid , m , n)
        self.dfs(i , j - 1 , grid , m , n)
        self.dfs(i , j + 1 , grid , m , n)
        self.dfs(i + 1 , j , grid , m , n)
        