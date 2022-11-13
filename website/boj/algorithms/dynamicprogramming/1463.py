"""
이건 해봤지 :)
F(N) = min(F(N//2), F(N//3), F(N-1)) + 1 
    단, 2나 3으로 나누어 떨어질 경우에만. 
input: 1e6보다 작거나 같은 정수 N

Python3  46468	640
PyPy3	131096	156

other
python	30864	60 ??????????????
"""


# 1로 만들기
# https://www.acmicpc.net/problem/1463
def sol_1463():
    d = [0, 0, 1, 1]+[0] * 999997
    N = int(input())
    for i in range(4, N+1):
        d[i] =  d[i-1] + 1
        if i%2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
    print(d[N])
    pass


# https://www.acmicpc.net/problem/status/1463/1003/1
def other_1463():
    pass



