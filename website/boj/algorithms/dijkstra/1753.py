
# 최단경로
# https://www.acmicpc.net/problem/1753
def sol_1753():
    from sys import stdin
    import heapq

    input = stdin.readline
    V, E = map(int, input().split())
    start = int(input())
    graph = {v:[] for v in range(1, V+1)}
    INF = int(4e6)
    d = [INF] * (V+1)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v,w))

    d[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        curr_d, curr_node = heapq.heappop(q)
        if curr_d > d[curr_node]:
            continue
        
        for node, weight in graph[curr_node]:
            c = curr_d + weight
            if d[node] <= c: # 등호를 빼면 python은 시간초과 나옴
                continue
            else:
                d[node] = c
                heapq.heappush(q, (c, node))
        pass

    for dist in d[1:]:
        print("INF" if dist == INF else dist)


# https://www.acmicpc.net/problem/status/1753/1003/1
def other_1753():
    pass



