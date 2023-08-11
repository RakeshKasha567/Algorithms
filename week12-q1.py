from collections import deque

def hasPath(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    queue = deque([start])
    visited = set([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == destination:
            return True

        for dx, dy in directions:
            newX, newY = x + dx, y + dy

            while is_valid(newX, newY):
                newX += dx
                newY += dy

            newX -= dx
            newY -= dy

            if (newX, newY) not in visited:
                queue.append((newX, newY))
                visited.add((newX, newY))

    return False

# Example test case
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
start = (0, 4)
destination = (4, 4)
print(hasPath(maze, start, destination))  # Output: True

maze2 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0]
]
start = (4, 3)
destination = (0, 1)
print(hasPath(maze, start, destination))  # Output: False
