
# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

# 32440	88
def sol_2667():
    from collections import Counter

    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    cnt = 1
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] != 1:
            return False
        graph[x][y] = -cnt
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    res = [v for i, v in Counter([v for li in graph for v in li if v]).items()]
    res.sort()
    print(cnt-1)
    for i in res:
        print(i)

# https://www.acmicpc.net/problem/status/2667/1003/1
    # 이 유형을 bfs로 했는데 속도가 빨라서 연구할 가치가 있을듯...
def other_2667():
    def isInside(x,y):
        return (0<=x<N and 0<=y<N)

    def bfs(start):
        queue=[start]
        y, x = start
        visit[y][x]=1
        count=0
        
        while queue:
            y, x = queue.pop(0)
            count=count+1
        
            dx=[0,0,1,-1]
            dy=[-1,1,0,0]
        
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if(isInside(nx,ny)):
                    if(house[ny][nx]==1 and visit[ny][nx]==0):
                        visit[ny][nx]=1
                        queue.append([ny,nx])
                    
        stack.append(count)

    N=int(input())

    house=[]
    for i in range(N):
        house.append(list(map(int, list(input()))))
        
    stack=[]
    visit=[[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            if(house[i][j]==1 and visit[i][j]==0):
                bfs([i,j])
                
    stack.sort()
    print(len(stack))
    for i in stack:
        print(i)


