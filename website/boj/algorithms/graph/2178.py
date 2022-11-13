
# 미로 탐색
# https://www.acmicpc.net/problem/2178
def sol_2178():
    import sys
    from collections import deque

    n, m = map(int, input().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    # graph = [list(map(int, input())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    def dfs(x, y):
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if nx == n-1 and ny == m-1:
                    return graph[x][y] + 1
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    print(dfs(0, 0))
        
# https://www.acmicpc.net/problem/status/2178/1003/1

def other_2178():
    pass



