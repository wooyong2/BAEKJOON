N = int(input())
if N == 1:
  print(1)
else:
  arr = [[0] for _ in range(N + 1)]
  arr[1], arr[2] = 1, 1
  for i in range(3, N + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

  print(arr[N])