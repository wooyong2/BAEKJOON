n, k = map(int, input().split())

dp = [[1] * k for _ in range(n)]

for i in range(k):
  dp[0][i] = i + 1

for i in range(1, n):
  for j in range(1, k):
    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[n - 1][k - 1] % 1000000000)