
# 지름길
# https://www.acmicpc.net/problem/1446
def sol_1446():
    import sys
    import heapq
    input = sys.stdin.readline
    
    n, d = map(int, input().split())
    vertex = {}
    # distance = list(range(d+1))
    q = []
    for _ in n:
        s, e, c = map(int, input().split())
        vertex.update([s, e])
        q = heapq.heappush(c+s-e, s, e)
    vertex = list(vertex)
    distance = {v: v for v in vertex}

    


    pass


# https://www.acmicpc.net/problem/status/1446/1003/1
def other_1446():
    pass



