
# 숨바꼭질
# https://www.acmicpc.net/problem/169
# 시간초과..:(
def sol_1697():
    from collections import deque
    
    n, k = map(int,input().split())
    res = {}
    cases = ['+1', '-1', '*2']
    while k not in res:

        pass
    def bfs(v, l):
        q1 = deque([(v, 0)])
        q2 = deque([l, 0])
        while q1 or q2:
            curr1, step1 = q1.popleft()
            curr2, step2 = q2.popleft()
            if curr1 == curr2:
                return step1 + step2
            for case in cases:
                next1 = eval(f'{curr1}{case}')
                next2 = eval(f'{curr2}{case}')
                if next1 < 0:
                    continue
                q1.append((next1, step1+1))
    print(bfs(n))


def other_1697():
    pass



