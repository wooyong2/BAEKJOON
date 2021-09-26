import itertools
N, M = list(map(int, input().split()))
N_list = list(range(1, N + 1))

ans_list = list(itertools.permutations(N_list, M))

for ans in ans_list:
    ans = list(ans)
    for i in ans:
        print(i, end=' ')
    print()