T = int(input())
ans = [[0] for _ in range(11)]
ans[1], ans[2], ans[3] = 1, 2, 4

for i in range(4, 11):
  ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

for i in range(T):
  print(ans[int(input())])