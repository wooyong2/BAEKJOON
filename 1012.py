def dfs(x, y):
    visited[x][y] = 1
    global cnt
    # 배추가 있으면 1 카운트
    if farm[x][y] == 1:
        cnt += 1
    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if visited[nx][ny] == 0 and farm[nx][ny] == 1:
                dfs(nx, ny)
                
                
# 방향 확인을 위한 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                            
T = int(input())
for i in range(T):
    M, N, K = list(map(int, input().split()))
    farm = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for j in range(K):
        x, y = list(map(int, input().split()))
        farm[x][y] = 1
    cnt = 0
    cnt_list = []
    
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt_list.append(cnt)
                cnt = 0
    print(len(cnt_list))
