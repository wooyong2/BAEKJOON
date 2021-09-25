from collections import deque

m, n = map(int, input().split())
box = []
queue = deque([])

for i in range(n):
  box.append(list(map(int, input().split())))
  for j in range(len(box[i])):
    if box[i][j] == 1:
      queue.append([i, j])

def bfs(box):
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
        queue.append([nx, ny])
        box[nx][ny] = box[x][y] + 1

bfs(box)
ans = 0

for row in box:
  for col in row:
    if col == 0:
      print(-1)
      quit()
  ans = max(max(row), ans)

print(ans - 1)