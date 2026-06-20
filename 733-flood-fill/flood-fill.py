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

            for adjacent in self.see_adjacent(image, x, y, original_color):
                if adjacent not in visited:
                    queue.append(adjacent)
        
        return image


    def see_adjacent(self, image: List[List[int]], x: int, y: int, original_color: int) -> List[Tuple[int]]:
        N = len(image)
        M = len(image[0])
        adjacents = []
        if x > 0 and image[x-1][y] == original_color:
            adjacents.append((x-1,y))
        if y > 0 and image[x][y-1] == original_color:
            adjacents.append((x,y-1))
        if x < N - 1 and image[x+1][y] == original_color:
            adjacents.append((x+1,y))
        if y < M - 1 and image[x][y+1] == original_color:
            adjacents.append((x,y+1))
        return adjacents
        