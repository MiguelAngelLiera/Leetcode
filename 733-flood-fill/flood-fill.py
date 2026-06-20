class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        visited = set()
        queue = deque()
        queue.append((sr, sc))

        while queue:
            x, y = queue.popleft()
            image[x][y] = color
            visited.add((x, y))

            self.add_adjacent(image, x, y, original_color, visited, queue)
        
        return image


    def add_adjacent(self, image: List[List[int]], x: int, y: int, original_color: int, visited: set, queue):
        N = len(image)
        M = len(image[0])
        if x > 0 and image[x-1][y] == original_color:
            adjacent = (x-1,y)
            if adjacent not in visited:
                queue.append(adjacent)
        if y > 0 and image[x][y-1] == original_color:
            adjacent = (x,y-1)
            if adjacent not in visited:
                queue.append(adjacent)
        if x < N - 1 and image[x+1][y] == original_color:
            adjacent = (x+1,y)
            if adjacent not in visited:
                queue.append(adjacent)
        if y < M - 1 and image[x][y+1] == original_color:
            adjacent = (x,y+1)
            if adjacent not in visited:
                queue.append(adjacent)
        