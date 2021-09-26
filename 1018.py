N, M = list(map(int, input().split()))
min_erase = N * M
board = [0 for _ in range(N)]

W = "WBWBWBWB"
B = "BWBWBWBW"
standard_W = []
standard_B = []

for i in range(8):
    if i % 2 == 0:
        standard_W.append(W)
        standard_B.append(B)
    else:
        standard_W.append(B)
        standard_B.append(W)
        
for i in range(N):
    board[i] = input()

for p in range(M - 7):
    for i in range(N - 7):
        sample = []
        case_1 = 0
        case_2 = 0
        for j in range(i, i + 8):
            sample.append(board[j][p:p + 8])
            
        for x in range(8):
            for y in range(8):
                if sample[x][y] != standard_W[x][y]:
                    case_1 += 1
                if sample[x][y] != standard_B[x][y]:
                    case_2 += 1
        if min(case_1, case_2) < min_erase:
            min_erase = min(case_1, case_2)
            
print(min_erase)
