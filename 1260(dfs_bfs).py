from collections import deque

N, M, V = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
visited_d = [False] * (N + 1)
visited_b = [False] * (N + 1)

for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(graph, v, visited_d):
    # 현재 노드를 방문 처리
    visited_d[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)


def bfs(graph, start, visited_b):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited_b[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 노드의 인접노드 중에서 아직 방문하지 않은 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True


dfs(graph, V, visited_d)
print()
bfs(graph, V, visited_b)