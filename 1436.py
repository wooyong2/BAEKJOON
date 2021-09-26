N = int(input())
cnt = 0
end_num = []
for i in range(10000666):
    if "666" in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break