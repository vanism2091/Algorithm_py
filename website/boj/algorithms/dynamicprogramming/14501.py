
"""
퇴사.
상담 Ti, Pi, 시간 / 페이
0 1 2 3 4 5 6
3 5 1 1 2 4 2

2 5 2 3 5
N=1일 때, 0 -> 3-1인 f(2)일때 계산
N=2일 때, 0
N=3일 때, 10 -> f(0) max( 0까지의max+ 0 스코어, 이전max+3score)
...
N=6일 때, f(6) = max(d[:2]+s_2, d[:5]) 

n일에 마치는, 다양한 n-i들이 있을거임.. 그것들 중 max를 구하면 될듯

N=i일 때, 

"""
# 퇴사
# https://www.acmicpc.net/problem/14501
def sol_14501():
    scd = [[] for _ in range(15)]
    N = int(input())
    for i in range(N):
        t, p = map(int, input().split())
        scd[i+t-1].append((i, p))    
    d = [0] * 15
    if scd[0]: d[0] = scd[0][0][1]
    for i in range(1, N):
        candi = [d[i-1]]
        for idx, p in scd[i]:
            if idx == 0:
                candi.append(p)
            else:
                candi.append(d[idx-1]+p)
        d[i] = max(candi)
    print(d[N-1])


# https://www.acmicpc.net/problem/status/14501/1003/1
def other_14501():
    pass



