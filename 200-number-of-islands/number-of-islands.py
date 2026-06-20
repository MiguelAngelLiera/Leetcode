class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        visited = set()
        islands = 0

        for x in range(N):
            for y in range(M):
                if  grid[x][y] == "1" and (x, y) not in visited:
                    self.dfs(x, y, grid, visited)
                    islands += 1
        return islands


    def dfs(self, sr:int, sc: int, grid: List[List[str]], visited: Set[Tuple[int]]) -> None:
        visited.add((sr, sc))
        self.iterate_adjacents(sr, sc, grid, visited)


    
    def iterate_adjacents(self, x:int, y: int, grid: List[List[str]], visited: Set[Tuple[int]]) -> None:
        N = len(grid)
        M = len(grid[0])

        if x > 0 and grid[x-1][y] == "1" and (x-1, y) not in visited:
            self.dfs(x-1, y, grid, visited)
        if y > 0 and grid[x][y-1] == "1" and (x, y-1) not in visited:
            self.dfs(x, y-1, grid, visited)
        if x < N - 1 and grid[x+1][y] == "1" and (x+1, y) not in visited:
            self.dfs(x+1, y, grid, visited)
        if y < M - 1 and grid[x][y+1] == "1" and (x, y+1) not in visited:
            self.dfs(x, y+1, grid, visited)


    # def bfs(self, sr:int, sc: int, grid: List[List[str]], visited: Set[Tuple[int]]) -> None:
    #     q = deque()
    #     q.append((sr,sc))

    #     while q:
    #         x, y = q.popleft()
    #         visited.add((x, y))

    #         self.add_adjacents(x, y, grid, visited, q)


    # def add_adjacents(self, x:int, y: int, grid: List[List[str]], visited: Set[Tuple[int]], queue) -> None:
    #     N = len(grid)
    #     M = len(grid[0])

    #     if x > 0 and grid[x-1][y] == "1" and (x-1, y) not in visited:
    #         queue.append((x-1, y))
    #     if y > 0 and grid[x][y-1] == "1" and (x, y-1) not in visited:
    #         queue.append((x, y-1))
    #     if x < N - 1 and grid[x+1][y] == "1" and (x+1, y) not in visited:
    #         queue.append((x+1, y))
    #     if y < M - 1 and grid[x][y+1] == "1" and (x, y+1) not in visited:
    #         queue.append((x, y+1))
        


        