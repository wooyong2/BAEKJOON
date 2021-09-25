import sys

input = sys.stdin.readline

n = int(input())
min_arr = [0] * 3
max_arr = [0] * 3
for _ in range(n):
  a, b, c = map(int, input().split())
  min_arr[0], min_arr[1], min_arr[2] = min(min_arr[0] + a, min_arr[1] + a), min(min_arr[0] + b, min_arr[1] + b, min_arr[2] + b), min(min_arr[1] + c, min_arr[2] + c)
  max_arr[0], max_arr[1], max_arr[2] = max(max_arr[0] + a, max_arr[1] + a), max(max_arr[0] + b, max_arr[1] + b, max_arr[2] + b), max(max_arr[1] + c, max_arr[2] + c)

print(max(max_arr), min(min_arr))