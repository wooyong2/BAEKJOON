import heapq

n = int(input())
card = []
for _ in range(n):
  heapq.heappush(card, int(input()))

if len(card) == 1:
  print(0)
else:
  ans = 0
  while len(card) > 1:
    tmp_1 = heapq.heappop(card)
    tmp_2 = heapq.heappop(card)
    ans += tmp_1 + tmp_2
    heapq.heappush(card, tmp_1 + tmp_2)
  print(ans)