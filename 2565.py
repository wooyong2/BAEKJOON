from operator import itemgetter
n = int(input())
lines = []
for i in range(n):
    lines.append(list(map(int, input().split())))

lines.sort(key=itemgetter(0))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))