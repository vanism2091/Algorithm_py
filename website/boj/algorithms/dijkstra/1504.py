"""
    dijkstra를 두 번 수행
    1. 1부터 v1까지
    2. v2부터 N까지
    3. 1 + 2 + v1-v2
"""
# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504
def sol_1504():
    import sys
    import heapq

    def sol():
        input = sys.stdin.readline
        N, E = map(int,input().split())
        graph = [[] for _ in range(N+1)]
        INF = int(1e9)
        # graph 입력 받기
        for _ in range(E):
            a, b, c = map(int, input().split())
            graph[a].append((c, b))
            graph[b].append((c, a))
            
        v1, v2 = map(int,input().split())
            
        def dijkstra(start, end):
            # start에서 end까지의 최단 거리를 구하는 dijkstra
            # q, d 초기화
            q = []
            d = [INF] * (N+1)
            d[start] = 0
            heapq.heappush(q, (0, start))
            while q:
                curr_c, curr_node = heapq.heappop(q)
                if curr_c > d[curr_node]:
                    continue
                if curr_node == end:
                    # end node를 만나면 return 한다
                    return curr_c
                for dist, node in graph[curr_node]:
                    c = curr_c + dist
                    if d[node] > c:
                        d[node] = c
                        heapq.heappush(q, (c, node))
            return -1 if d[end] == INF else d[end]
        
        if not E: return -1

        mid_dist = -1
        for dist, node in graph[v1]:
            if node == v2:
                mid_dist = dist
        if mid_dist == -1: return -1
            
        res1, res2 = dijkstra(1, v1), dijkstra(v2, N)
        res3, res4 = dijkstra(1, v2), dijkstra(v1, N)
        total = INF
        if res1 != -1 and res2 != -1:
            total = res1 + res2
        if res3 != -1 and res4 != -1:
            total = min(total, res3+res4)
        if total == INF:
            return -1
        else: 
            return total+mid_dist

    print(sol())



# https://www.acmicpc.net/problem/status/1504/1003/1
def other_1504():
    pass



