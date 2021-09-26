n = int(input())
wine_list = [0]
for _ in range(n):
    wine_list.append(int(input()))
    
dp = [0]
dp.append(wine_list[1])
if (n > 1):
    dp.append(wine_list[1] + wine_list[2])
    
# 1: 이번 포도주를 마시고 이전 포도주를 마시지 않은 경우
# 2: 이번 포도주를 마시고 이전 포도주도 마신 경우
# 3: 이번 포도주를 마시지 않아야 하는 경우

for i in range(3, n + 1):
    case_1 = wine_list[i] + dp[i - 2]
    case_2 = wine_list[i] + wine_list[i - 1] + dp[i - 3]
    case_3 = dp[i - 1]
    
    dp.append(max(case_3, case_2, case_1))

print(dp[n])