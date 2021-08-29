# 백준 1463번

N = int(input())
dp = [0 for _ in range(N + 1)]
dp[1] = 0

for i in range(2, N + 1):

    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어질 때 2로 나누는 경우가 1을 빼는 것보다 연산 횟수가 적으면 교체
    if i % 2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1

    # 3으로 나누어 떨어질 때 위의 두 연산보다 3으로 나눈 것이 연산 횟수가 적으면 교체
    if i % 3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1

print(dp[N])