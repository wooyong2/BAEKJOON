n = int(input())
town = []
for i in range(n):
    town.append(list(map(int, input())))

visited = [[0]*n for _ in range(n)]

# 방향 확인을 위한 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                
def dfs(x, y):
    visited[x][y] = 1
    global cnt
    # 아파트가 있으면 1 카운트
    if town[x][y] == 1:
        cnt += 1
    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and town[nx][ny] == 1:
                dfs(nx, ny)
                
                
cnt = 0
cnt_list = []

for i in range(n):
    for j in range(n):
        if town[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            cnt_list.append(cnt)
            cnt = 0

print(len(cnt_list))
for ans in sorted(cnt_list):
    print(ans)