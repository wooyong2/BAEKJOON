N = int(input())
seq = list(map(int, input().split()))
len_list = [0 for _ in range(N)]
len_list[0] = 1
for i in range(len(seq)):
    tmp_list = []
    for j in range(i):
        if seq[j] < seq[i]:
            tmp_list.append(len_list[j] + 1)
    if tmp_list:
        len_list[i] = max(tmp_list)
    else:
        len_list[i] = 1

print(max(len_list))