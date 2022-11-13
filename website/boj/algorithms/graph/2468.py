
# 안전 영역
# https://www.acmicpc.net/problem/2468

"""
안전영역
이거 그래프 + binary serch일까..?
input: 
    - 1. N [2, 100] 행과 열의 갯수
    - 행의 높이 정보

1차 시도 틀린 이유: 그래프 바꿔놓고 초기화를 안했음 ㅋㅋ
2차 시도는 그래프 + bs로 해보자

bs로 안될거같음.. bs 문제는 start, end를 조정하면
기준에 따라서 값이 모노토닉하게 바뀌는데
    - 예를 들어 자르는 길이를 늘리면 갖고가는 떡의 길이는 무조건 늘어난다
    - 길이가 넘치면 start조정, 길이가 모자라면 end를 조정했다.
    그런데 이 문제의 경우, 높이가 높아짐에 따라, 
    안전 영역의 갯수는 늘어났다가 다시 낮아진다 완전탐색?해야하나?
    bs 구현 생각은 버리고 그래프 초기화나 해보자

그래프 초기화를 했고, 몇 번 틑렸는데 이유
    1. recursionError
    2. res의 if문. 반복 탈출문의 문제
    즉, convex function이 아니었던거임!!!!

Python3     38924	1088
PyPy3       메모리 초과
"""
# 틀렸습니다 :(
def sol_2468():
    def try_1():
        from collections import Counter
        import sys
        sys.setrecursionlimit(10**6)

        n = int(input())
        c = Counter()
        graph = []
        for i in range(n):
            graph.append(list((map(int, input().split()))))
            c.update(graph[i])

        def dfs(x, y, visited):
            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                return False
            visited[x][y] = 1
            dfs(x-1, y, visited)
            dfs(x+1, y, visited)
            dfs(x, y-1, visited)
            dfs(x, y+1, visited)
            return True

        def get_num(visited):
            cnt = 0
            for i in range(n):
                for j in range(n):
                    if dfs(i, j, visited):
                        cnt += 1
            return cnt

        res = [0]*len(c)
        for idx, i in enumerate(sorted(list(c))):
            visited = [[0 if e>i else 1 for e in li] for li in graph]
            curr_res = get_num(visited)
            print(res)
            if res[idx-1] >= curr_res:
                break
            res[idx] = curr_res
        print(max(*res, 1))

# TODO: 이건 진짜 해야함ㅋㅋㅋㅋ
def other_2468():
    def other_1():
        import sys
        from collections import defaultdict

        N = int(sys.stdin.readline())
        d = defaultdict(list)

        for i, row in enumerate(sys.stdin.readlines()):
            for j, v in enumerate(map(int, row.split())):
                d[v].append((i, j))

        parents = [[0]*N for _ in range(N)]

        def get_root(coor):
            p = parents[coor[0]][coor[1]]
            temp = []
            while p != coor:
                temp.append(coor)
                p, coor = parents[p[0]][p[1]], p
            for i, j in temp:
                parents[i][j] = p
            return p

        answer = 1
        n = 0

        for v in sorted(d, reverse=True)[:-1]:
            for i, j in d[v]:
                connected = set()
                for i_, j_ in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if 0 <= i_ < N and 0 <= j_ < N and parents[i_][j_] != 0:
                        connected.add(get_root((i_, j_)))
                if len(connected) == 0:
                    n += 1
                    parents[i][j] = (i, j)
                elif len(connected) == 1:
                    parents[i][j] = connected.pop()
                else:
                    root = connected.pop()
                    n -= len(connected)
                    parents[i][j] = root
                    for coor in connected:
                        parents[coor[0]][coor[1]] = root

            if answer < n:
                answer = n

        print(answer)
    def other_2():
        import sys
        from collections import defaultdict
        input = sys.stdin.readline

        root = {}
        W = 0

        def find(x):
            """
            목표: x의 root를 찾는다.
            - 경로압축: x에서 root까지의 모든 노드의 root를 찾는다. 
            """
            if root[x] == x:
                return x
            root[x] = find(root[x])
            return root[x]

        def union(r1, r2):
            """
            목표: 두 root를 하나로 합친다. (r2를 r1 아래에 둔다.)
            """
            root[find(r2)] = find(r1)

        def adj(p):
            yield p - W
            yield p - 1
            yield p + 1
            yield p + W

        def main():
            global W
            N = int(input())
            P = 1 # 4방향 패딩
            W = N + 2*P # 한 열의 너비

            h2i = defaultdict(list) # 높이별 위치의 인덱스
            for r in range(P, N+P):
                heights_line = list(map(int, input().split()))
                for h, i in zip(heights_line, range(r*W+1, (r+1)*W-1)):
                    h2i[h].append(i)
            heights = sorted(h2i, reverse=True)[:-1] # 최고 높이 heights[-1]일 때는 모두 잠김, cnt = 0
            cnt = 1 # 물의 높이가 0이거나, 모든 땅의 높이보다 작을 때는 cnt = 1(= min_cnt)
            rep = []
            for h in heights: # 물의 높이 <- 땅의 높이 h
                # root 초기화
                for i in h2i[h]:
                    root[i] = i
                
                # 현재 위치(인덱스)를 특정 인접 위치들의 root로 만든다.
                # 인접 위치가 root를 가져야 한다.
                # - 현재 높이의 위치들
                # - 이전 높이의 위치들
                for i in h2i[h]:
                    for j in adj(i):
                        if j in root:
                            union(i, j)
                # 스스로 root인 위치를 구역의 대표로 사용한다.
                # - 이전까지의 대표 중, 아직도 대표인 것
                rep = [i for i in rep if root[i] == i]
                # - 현재 높이의 위치 중, 대표인 것
                for i in h2i[h]:
                    if root[i] == i:
                        rep.append(i)
                cnt = max(cnt, len(rep))

            print(cnt)

        main()


