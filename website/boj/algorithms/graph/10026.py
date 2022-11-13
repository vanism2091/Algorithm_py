
# 적록색약
# https://www.acmicpc.net/problem/10026

def sol_10026():
    n = int(input())
    graph = []
    dic = {"R": -1, "G": 1, "B": 0}
    for _ in range(n):
        graph.append([dic[i] for i in input()])

    def get_num(is_abs):
        def dfs(x, y, curr):
            if x<0 or x>= n or y<0 or y>= n:
                return
            if is_abs:
                if abs(graph[x][y]) != curr: return
            else:
                if graph[x][y] != curr: return
            if visited[x][y]:
                return
            visited[x][y] = 1
            dfs(x-1, y, curr)
            dfs(x+1, y, curr)
            dfs(x, y-1, curr)
            dfs(x, y+1, curr)
            pass

        visited = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    dfs(i, j, graph[i][j])
                    cnt += 1
        return cnt
    print(get_num(False))
    print(get_num(True))
    
    # R : 114
    # G : 103
    # B : 98


# https://www.acmicpc.net/problem/status/10026/1003/1
    
## 내 속도 90쯤, 이분은 72
def other_10026():
    import sys
    sys.setrecursionlimit(10**6)
    n=int(input())
    a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]
    b=[i.copy()for i in a]
    def cnt(s,x,y,c):
        s[x][y]=" "
        if s[x-1][y]==c:cnt(s,x-1,y,c)
        if s[x+1][y]==c:cnt(s,x+1,y,c)
        if s[x][y-1]==c:cnt(s,x,y-1,c)
        if s[x][y+1]==c:cnt(s,x,y+1,c)
    c=d=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][j]!=" ":
                cnt(a,i,j,a[i][j]);c+=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if b[i][j]=="G":b[i][j]="R"
    for i in range(1,n+1):
        for j in range(1,n+1):
            if b[i][j]!=" ":
                cnt(b,i,j,b[i][j]);d+=1
    print(c,d)
