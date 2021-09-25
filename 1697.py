from collections import deque

def bfs(q, k):
  dist = [0] * 100001
  while q:
    x = q.popleft()
    if x == k:
      print(dist[x])
      break
    for nx in (x - 1, x + 1, 2*x):
      if 0 <= nx < 100001 and dist[nx] == 0:
        dist[nx] = dist[x] + 1
        q.append(nx)

n, k = map(int, input().split())
queue = deque([n])
bfs(queue, k)