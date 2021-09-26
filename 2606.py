N = int(input())
M = int(input())
v = 1

graph = [[] for _ in range(N + 1)]
visited_d = [False] * (N + 1)

for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


def dfs(graph, v, visited_d):
    # 현재 노드를 방문 처리
    visited_d[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)


dfs(graph, v, visited_d)
print(visited_d.count(True) - 1)
