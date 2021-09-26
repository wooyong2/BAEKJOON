test_case = int(input())
distances = []
for i in range(test_case):
    x, y = list(map(int, input().split()))
    distances.append(y - x)

for d in distances:
    n = 1
    while True:
        if d <= n * (n + 1):
            if d <= n * n:
                print(2 * n - 1)
            else:
                print(2 * n)
            break
        n += 1