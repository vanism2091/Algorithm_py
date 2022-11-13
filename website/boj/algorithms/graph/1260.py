
# DFS와 BFS
# https://www.acmicpc.net/problem/1260
#
# input:
#   첫째 줄에 정점의 개수 N [1,1000], 간선의 개수 M [1,10,000], 탐색을 시작할 정점의 번호 V가 주어진다. 
#   다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
#   어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 내 IDEA
# list로 해도 될 것 같은데, 정점갯수 1이고 정점이 1000인 경우 메모리 낭비..
# 그래프 표현은 dictionary로 하자. {"node":[linked nodes]}
# visited도 dictionary {"node": True/False}
# 예외 케이스 :: v가 m에 없는 경우가 있었다 :)
# 34032	480 처참한 속도..:)
def sol_1260():
    n, m, v = map(int, input().split())
    graph = {}
    visited = {}

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, input().split())
        if i not in graph:
            graph[i] = [j]
            visited[i] = False
        else : graph[i].append(j)
        if j not in graph:
            graph[j] = [i]
            visited[j] = False
        else: graph[j].append(i)

    def dfs(v):
        # if not visited[v]:
        #     return
        visited[v] = True
        print(v, end=" ")
        for i in sorted(graph[v]):
            if visited[i]:
                continue
            dfs(i)
    dfs(v)
    print()
    for k in visited:
        visited[k] = False
    from collections import deque
    def bfs(v):
        q = deque([v])
        visited[v] = True
        while q:
            # print(q)
            i = q.popleft()
            print(i, end=" ")
            for n in sorted(graph[i]):
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)

def sol_1260_n():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    def dfs(v):
        visited[v] = True
        print(v, end=" ")
        for i in sorted(graph[v]):
            if visited[i]:
                continue
            dfs(i)
    dfs(v)

    visited = [False]*(n+1)
    from collections import deque
    def bfs(v):
        visited[v] = True
        q = deque([v])
        while q:
            i = q.popleft()
            print(i, end=" ")
            for n in sorted(graph[i]):
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)

    # 속도 차이가 너무 남...
    # 1. sys.stdin.readline().split()       :: 와... 480 -> 100 미쳤따..
    # 2. graph sort를 미리 한다 > 기존은 bfs, dfs 2번에 걸쳐서 함. :: dictionary의 경우 큰 속도 차이 없음;
    # 3. print를 계속 하지 말고 res list를 나중에 한꺼번에 프린트한다 :: 100 -> 100 ㄴㄴ

def sol_1260_last_dict():
    import sys
    from collections import deque

    n, m, v = map(int, input().split())
    graph = {}
    visited = {}

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        if i not in graph:
            graph[i] = [j]
            visited[i] = False
        else : graph[i].append(j)
        if j not in graph:
            graph[j] = [i]
            visited[j] = False
        else: graph[j].append(i)

    for k in graph:
        graph[k].sort()

    res_dfs = []
    def dfs(v):
        if v not in visited:
            res_dfs.append(v)
            return
        visited[v] = True
        res_dfs.append(v)
        for i in graph[v]:
            if visited[i]:
                continue
            dfs(i)
    dfs(v)
    print(*res_dfs)
    for k in visited:
        visited[k] = False

    res_bfs = []
    def bfs(v):
        if v not in visited:
            res_bfs.append(v)
            return
        q = deque([v])
        visited[v] = True
        while q:
            i = q.popleft()
            res_bfs.append(i)
            for n in graph[i]:
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)
    print(*res_bfs)

