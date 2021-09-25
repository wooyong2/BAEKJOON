import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y):
  if x == 0 and y == 0:
    return 1
  if dp[x][y] == -1:
    dp[x][y] = 0
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if arr[x][y] < arr[nx][ny]:
          dp[x][y] += dfs(nx, ny)
          
  return dp[x][y]


m, n = map(int, input().split())
arr = []
for _ in range(m):
  arr.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1] * n for _ in range(m)]

print(dfs(m - 1, n - 1))