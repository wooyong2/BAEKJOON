import sys

input = sys.routedin.readline

n = int(input())
m = int(input())

route = []
rid = []

for i in range(m):
  a, b = map(int, input().split())
  if a < b:
    route.append([a, b, i + 1])
  else:
    route.append([a - n, b, i + 1])
    route.append([a, b + n, i + 1])

route.sort(key=lambda x: (x[0], -x[1]))

routed = route[0]
for i in range(1, len(route)):
  if route[i][1] > routed[1]:
    routed = route[i]
  else:
    rid.append(route[i][2])

rid = set(rid)
ans = set(range(1, m + 1))
ans = list(ans - rid)
ans.sort
print(*ans)