## TODO: 다른 분 풀이 분석해보기


# 유기농 배추
# https://www.acmicpc.net/problem/1012
# 328 -> 80 sys.stdin.readline 
def sol_1012():
    import sys
    p=sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(p())
    def get_num(n, m, graph):
        def dfs(x, y):
            if x<0 or x>= n or y<0 or y>= m:
                return False
            if graph[x][y] == 0:
                return False
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        cnt = 0
        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    cnt += 1
        return cnt
        
    for _ in range(n):
        m, n, k = map(int, p().split())
        graph = [[0]*m for _ in range(n)]
        for _ in range(k):
            y, x = map(int,p().split())
            graph[x][y] = 1
        print(get_num(n, m, graph))

## TODO: 분석해보기
def other_1012():
    import sys;p=sys.stdin.readline;
    sys.setrecursionlimit(1000000)
    q=int(p())
    def T(t, o, s):
        t[s][o]=0
        if o+1 < x and t[s][o+1]==1:
            T(t,o+1,s)
        if o-1>= 0 and t[s][o-1]==1:
            T(t, o-1,s)
        if s -1 >= 0 and t[s-1][o]==1:
            T(t, o,s-1)
        if s +1 < y and t[s+1][o]==1:
            T(t,o,s+1)

    for _ in range(q):
        x, y, c = map(int, p().split())
        t = [[0] * x for _ in range(y)]
        for i in range(0,c):
            m,n=map(int,p().split());t[n][m] = 1
        v = 0
        for i in range(0,x):
            for j in range(0, y):
                if t[j][i] == 1:
                    T(t, i, j);v+=1
        print(v)

