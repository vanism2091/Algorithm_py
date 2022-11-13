# need to solve
# 맞히면 other도 보기

# 토마토
# https://www.acmicpc.net/problem/7576

"""
토마토
- 1이 몇 개인지, 어디에 있는지 알아야 하고 (시작 지점)
- bfs를 하면서 상하좌우는 이전 step의 +1
- 그런데 다른 토마토도 있을 테니 만약 0이 아니면 min(step+1, value)
- 만약 min이후 step+1이 아니라 value라면, 그 방향으로는 그만 append
- 전체 상자 내에서 최댓값을 프린트
- 끝났는데 0이 있으면 -1을 출력

- 시간초과 :(
    5% index마다 bfs 쭉..
    44% 1 있는 만큼 q 리스트를 만들어서 depth마다 q를..

아아.. 44%... 
약속의 PyPy3으로 돌려보자
44에서 마찬가지로 문제가 생긴다. 종료 조건이 있어야 하나? 무한 루프에 빠진걸까?
생각해보니 -1 처리를 안했음 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
"""
def sol_7576_1():
    import sys
    from collections import deque

    p = sys.stdin.readline
    m, n = map(int, p().split())
    idxs = []
    graph = []

    # 그래프 초기화
    for i in range(n):
        l = list(map(int,p().split()))
        graph.append(l)
        if 1 not in l:
            continue
        for j, v in enumerate(l):
            if v == 1: idxs.append((i, j))
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS 정의
    def bfs(i, j, cnt):
        q = deque([(i, j)])
        while q:
            print(cnt, q)
            cnt += 1
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                c = graph[nx][ny]; b = graph[x][y]+1
                if c == 0 or c > b:
                    graph[nx][ny] = b
                    q.append((nx, ny))
                elif c <= b:
                    continue
    for x, y in idxs:
        bfs(x, y, cnt)
    res = [v for l in graph for v in l]
    if 0 in res:
        print(-1)
    else:
        print(max(res)-1)


def sol_7576_2():
    import sys
    from collections import deque

    inputs = sys.stdin.read().splitlines()
    m, n = map(int, inputs[0].split())
    idxs = []
    graph = []

    # 그래프 초기화
    for i in range(n):
        l = list(map(int,inputs[1+i].split()))
        graph.append(l)
        if 1 not in l:
            continue
        for j, v in enumerate(l):
            if v == 1: idxs.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS 정의
    def bfs(idxs):
        # 모든 1들에 대해 deque를 만든다
        qs = [deque([(x, y)]) for x, y in idxs]
        while qs:
            for q in qs:
                if not q:
                    qs.remove(q)
                    continue
                x, y = q.popleft()
                stop_traverse_idx = set()
                for i in range(4):
                    if i in stop_traverse_idx:
                        continue
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    c = graph[nx][ny]; b = graph[x][y]+1
                    if c == 0 or c > b:
                        graph[nx][ny] = b
                        q.append((nx, ny))
                    elif c <= b or c == -1:
                        stop_traverse_idx.add(i)
                        if len(stop_traverse_idx) == 4:
                            break
                        continue
    bfs(idxs)
    res = [v for l in graph for v in l]
    if 0 in res:
        print(-1)
    else:
        print(max(res)-1)

sol_7576_2()
def other_7576():
    pass



